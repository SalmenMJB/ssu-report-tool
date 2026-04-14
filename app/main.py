"""
Point d'entrée principal : génère tous les graphiques SSU.

Usage :
    python -m app.main

Les graphiques sont sauvegardés dans output/charts/
"""

import os
import warnings

warnings.filterwarnings(
    "ignore",
    message="Workbook contains no default style, apply openpyxl's default",
)

from app.parsers.effectifs import parse_effectifs_file
from app.parsers.stats_standard import parse_stats_standard_file
from app.parsers.stat_activite import parse_stat_activite_file
from app.parsers.pssm import parse_pssm_file
from app.parsers.bilan_actions import parse_bilan_actions_file
from app.parsers.dspe import parse_dspe_file

from app.config.intervenants import MEDECINS, INFIRMIERES

from app.services.indicator_service import (
    compute_effectifs_indicators,
    compute_stats_standard_indicators,
    compute_stat_activite_indicators,
    compute_pssm_indicators,
    compute_bilan_actions_indicators,
    compute_css_indicators,
    compute_bilans_professionnels_indicators,
)

from app.charts.effectifs_charts import plot_evolution_effectifs
from app.charts.etablissements_charts import plot_top_etablissements
from app.charts.etablissements_conventionnes_charts import plot_etablissements_conventionnes
from app.charts.stats_standard_charts import plot_appels_par_mois
from app.charts.stat_activite_charts import (
    plot_consultations_par_centre,
    plot_top_motifs,
    plot_repartition_sexe,
)
from app.charts.activite_charts import (
    plot_visites_vaccinations,
    plot_top_nationalites,
    plot_handicap,
)
from app.charts.consultations_charts import plot_recap_consultations
from app.charts.bilans_professionnels_charts import plot_bilans_medecins_vs_infirmieres
from app.charts.pssm_charts import plot_pssm_sessions, plot_pssm_lastest_year
from app.charts.bilan_actions_charts import (
    plot_actions_par_theme,
    plot_bilan_actions_par_campus,
    plot_consommables_bilan_actions,
    plot_actions_par_site_lisible,
)
from app.charts.css_charts import plot_motifs_reels_css
from app.charts.amenagements_charts import plot_evolution_amenagements
from app.charts.repartition_amenagements_charts import plot_reparition_amenagements
from app.charts.motifs_medecine_generale_charts import plot_motifs_medecine_generale_charts
from app.charts.motifs_medecine_generale_bis import plot_motifs_medecine_generale_bis


def generate_all_charts():
    """Génère tous les graphiques à partir des fichiers de données disponibles."""

    os.makedirs("output/charts", exist_ok=True)

    print("=" * 60)
    print("  Génération des graphiques SSU")
    print("=" * 60)

    # --- Effectifs ---
    effectifs_path = "data/raw/evolution_etab_conventionnes.xlsx"
    if os.path.isfile(effectifs_path):
        print("\n[Effectifs] Chargement...")
        df_effectifs = parse_effectifs_file(effectifs_path)
        plot_evolution_effectifs(df_effectifs)
        plot_top_etablissements(df_effectifs)
        plot_etablissements_conventionnes()
        print("  ✅ Graphiques effectifs générés")
    else:
        print(f"  ⚠️  Fichier manquant : {effectifs_path}")

    # --- Statistiques standard ---
    stats_path = "data/raw/stats_standard_ssu.xlsx"
    if os.path.isfile(stats_path):
        print("\n[Stats standard] Chargement...")
        df_stats = parse_stats_standard_file(stats_path)
        plot_appels_par_mois(df_stats)
        print("  ✅ Graphiques stats standard générés")
    else:
        print(f"  ⚠️  Fichier manquant : {stats_path}")

    # --- Activité ---
    activite_path = "data/raw/stat_activite.xlsx"
    if os.path.isfile(activite_path):
        print("\n[Activité] Chargement...")
        df_activite = parse_stat_activite_file(activite_path)
        activite_stats = compute_stat_activite_indicators(df_activite)
        css_stats = compute_css_indicators(df_activite)
        bilans_professionnels_stats = compute_bilans_professionnels_indicators(
            df_activite, MEDECINS, INFIRMIERES
        )

        if activite_stats:
            plot_consultations_par_centre(activite_stats)
            plot_top_motifs(activite_stats)
            plot_repartition_sexe(activite_stats)
            plot_recap_consultations(activite_stats)
            if "visites_effectuees" in activite_stats and "vaccinations" in activite_stats:
                plot_visites_vaccinations(activite_stats)
            if "top_nationalites" in activite_stats:
                plot_top_nationalites(activite_stats)
            if "handicap" in activite_stats:
                plot_handicap(activite_stats)
            plot_motifs_medecine_generale_charts(df_activite)
            plot_motifs_medecine_generale_bis(activite_stats)

        if bilans_professionnels_stats:
            plot_bilans_medecins_vs_infirmieres(bilans_professionnels_stats)

        if css_stats:
            plot_motifs_reels_css(css_stats)

        plot_reparition_amenagements()
        print("  ✅ Graphiques activité générés")
    else:
        print(f"  ⚠️  Fichier manquant : {activite_path}")

    # --- PSSM ---
    pssm_path = "data/raw/recap_pssm.xlsx"
    if os.path.isfile(pssm_path):
        print("\n[PSSM] Chargement...")
        pssm_sheets = parse_pssm_file(pssm_path)
        pssm_stats = compute_pssm_indicators(pssm_sheets)
        if pssm_stats:
            plot_pssm_sessions(pssm_stats)
            plot_pssm_lastest_year(pssm_stats)
        print("  ✅ Graphiques PSSM générés")
    else:
        print(f"  ⚠️  Fichier manquant : {pssm_path}")

    # --- Bilan des actions ---
    bilan_actions_path = "data/raw/bilan_actions.xlsx"
    if os.path.isfile(bilan_actions_path):
        print("\n[Bilan actions] Chargement...")
        df_bilan_actions = parse_bilan_actions_file(bilan_actions_path)
        bilan_actions_stats = compute_bilan_actions_indicators(df_bilan_actions)
        if bilan_actions_stats:
            plot_actions_par_theme(bilan_actions_stats)
            plot_bilan_actions_par_campus(bilan_actions_stats)
            plot_consommables_bilan_actions(bilan_actions_stats)
            plot_actions_par_site_lisible(bilan_actions_stats)
        print("  ✅ Graphiques bilan actions générés")
    else:
        print(f"  ⚠️  Fichier manquant : {bilan_actions_path}")

    # --- Aménagements (données statiques) ---
    print("\n[Aménagements] Génération...")
    plot_evolution_amenagements()
    print("  ✅ Graphique aménagements généré")

    print("\n" + "=" * 60)
    print("✅ Tous les graphiques ont été générés dans output/charts/")
    print("=" * 60)


def main():
    """Point d'entrée principal."""
    generate_all_charts()


if __name__ == "__main__":
    main()
