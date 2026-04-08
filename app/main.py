import pandas as pd

from app.parsers.effectifs import parse_effectifs_file
from app.parsers.stats_standard import parse_stats_standard_file
from app.parsers.consommables import parse_consommables_file
from app.parsers.stat_activite import parse_stat_activite_file
from app.parsers.pssm import parse_pssm_file
from app.parsers.psy import parse_psy_file

from app.services.indicator_service import compute_effectifs_indicators
from app.services.indicator_service import compute_stats_standard_indicators
from app.services.indicator_service import compute_consommables_indicators
from app.services.indicator_service import compute_stat_activite_indicators
from app.services.indicator_service import compute_pssm_indicators


from app.charts.stats_standard_charts import plot_appels_par_mois
from app.charts.effectifs_charts import plot_evolution_effectifs
from app.charts.etablissements_charts import plot_top_etablissements
from app.charts.consommables_charts import plot_consommables
from app.charts.pssm_charts import plot_pssm_sessions
from app.charts.consommables_charts import plot_actions_par_campus
from app.charts.etablissements_conventionnes_charts import plot_etablissements_conventionnes
from app.charts.repartition_amenagements_charts import plot_reparition_amenagements
from app.charts.consultations_charts import plot_recap_consultations
from app.charts.motifs_medecine_generale_charts import plot_motifs_medecine_generale_charts
from app.charts.activite_charts import (
    plot_visites_vaccinations,
    plot_top_nationalites,
    plot_handicap,
)
from app.charts.stat_activite_charts import (
    plot_consultations_par_centre,
    plot_top_motifs,
    plot_repartition_sexe,
)
from app.charts.amenagements_charts import plot_evolution_amenagements
from app.charts.activite_medicale_charts import (
    plot_evolution_activite_medicale,
    plot_repartition_activite_medicale_annee,
)
from app.charts.bilans_charts import (
    plot_bilans_par_composante,
    plot_bilans_internationaux,
    plot_bilans_par_filiere,
)
from app.charts.motifs_medecine_generale_bis import plot_motifs_medecine_generale_bis
from app.charts.infirmier_charts import plot_repartition_activite_infirmiere
from app.charts.psy_charts import plot_delai_attente_psy
from app.charts.psy_charts import plot_problematique_psy
from app.charts.infirmier_charts import plot_activite_infirmiere_compare
from app.charts.psy_charts import plot_duree_suivi
from app.charts.prevention_charts import plot_actions_par_site_lisible
from app.charts.infirmier_charts import plot_repartition_activite_depuis_reel
# from app.charts.psy_charts import plot_duree_suivi_psy
# from app.charts.pssm_charts import plot_origine_stagiaires_pssm

import warnings
warnings.filterwarnings(
    "ignore",
    message="Workbook contains no default style, apply openpyxl's default"
)


#### Deux fonctions pour un affichage plus propre dans le terminal ####
def print_section(title: str):
    print(f"\n{'=' * 10} {title} {'=' * 10}\n")

def print_indicators(indicators: dict):
    for key, value in indicators.items():
        print(f"{key} :")
        print(value)
        print()


def main():
    #### Visualisations tableaux ####
    print_section("Activités")
    activite_path = "data/raw/stat_activite.xlsx"
    df_activite = parse_stat_activite_file(activite_path)
    print(df_activite.head())
    activite_stats = compute_stat_activite_indicators(df_activite)
    print_indicators(activite_stats)

    
    print_section("Effectifs")
    effectifs_path = "data/raw/evolution_etab_conventionnes.xlsx" 
    df_effectifs = parse_effectifs_file(effectifs_path)
    print(df_effectifs.head())
    effectifs_stats = compute_effectifs_indicators(df_effectifs)
    print_indicators(effectifs_stats)


    print_section("STATS STANDARD")
    stats_path = "data/raw/stats_standard_ssu.xlsx"
    df_stats = parse_stats_standard_file(stats_path)
    stats_stats = compute_stats_standard_indicators(df_stats)
    print_indicators(stats_stats)

    print_section("CONSOMMABLES")
    consommables_path = "data/raw/extraction_consommables_actions_24_25.xlsx"
    df_consommables = parse_consommables_file(consommables_path)
    print(df_consommables.head())
    print()
    consommables_stats = compute_consommables_indicators(df_consommables)
    print_indicators(consommables_stats)

    print_section("PSSM")
    pssm_path = "data/raw/recap_pssm.xlsx"
    pssm_sheets = parse_pssm_file(pssm_path)
    print("Onglets retenus :")
    print(list(pssm_sheets.keys()))
    print()
    pssm_stats = compute_pssm_indicators(pssm_sheets)
    print_indicators(pssm_stats)
    
    print_section("STATS Motifs Psy")
    psy_path = "data/raw/stats_psy.xlsx"
    df_psy = parse_psy_file(psy_path)
    print(df_psy.head())
    print(df_psy.columns.tolist())
    plot_problematique_psy(df_psy)
    print("Graphique généré : output/charts/problematique_psy.png")



    #### GRAPHIQUES ####
    plot_recap_consultations(activite_stats)
    print("Graphique généré : output/charts/recap_consultations.png")

    plot_visites_vaccinations(activite_stats)
    print("Graphiques générés : output/charts/visites.png + output/charts/vaccinations.png")

    plot_top_nationalites(activite_stats)
    print("Graphique généré : output/charts/top_nationalites.png")

    plot_handicap(activite_stats)
    print("Graphique généré : output/charts/handicap.png")

    plot_consultations_par_centre(activite_stats)
    print("Graphique généré : output/charts/consultations_par_centre.png")

    plot_top_motifs(activite_stats)
    print("Graphique généré : output/charts/top_motifs.png")

    plot_repartition_sexe(activite_stats)
    print("Graphique généré : output/charts/repartition_sexe.png")

    plot_appels_par_mois(df_stats)
    print("Graphique généré : output/charts/appels_par_mois.png")

    plot_evolution_effectifs(df_effectifs)
    print("Graphique généré : output/charts/evolution_effectifs.png")

    plot_top_etablissements(df_effectifs)
    print("Graphique généré : output/charts/top_etablissements.png")

    plot_consommables(consommables_stats)
    print("Graphique généré : output/charts/consommables.png")

    plot_pssm_sessions(pssm_stats)
    print("Graphique généré : output/charts/pssm_sessions.png")

    plot_actions_par_campus(consommables_stats)
    print("Graphique généré : output/charts/actions_par_campus.png")

    plot_etablissements_conventionnes()
    print("Graphique généré : output/charts/etablissements_conventionnes.png")

    plot_reparition_amenagements()
    print("Graphique généré : output/charts/repartition_amenagements.png")


    plot_evolution_amenagements()
    print("Graphique généré : output/charts/evolution_amenagements.png")


    historique_medical_path = "data/processed/historique_activite_medicale.csv"
    plot_evolution_activite_medicale(historique_medical_path)
    print("Graphique généré : output/charts/evolution_activite_medicale.png")
    plot_repartition_activite_medicale_annee(historique_medical_path)
    print("Graphique généré : output/charts/repartition_activite_medicale.png")


    df_bilans = df_activite[df_activite["motif"] == "Bilan de prévention"]
    plot_bilans_par_composante(df_bilans)
    print("Graphique généré : output/charts/bilans_par_composante.png")
    plot_bilans_internationaux(df_bilans)
    print("Graphique généré : output/charts/bilans_internationaux.png")
    plot_bilans_par_filiere(df_bilans)
    print("Graphique généré : output/charts/bilans_par_filiere.png")

    plot_motifs_medecine_generale_charts(df_activite)
    print("Graphique généré : output/charts/motifs_medecine_generale_charts.png")
    plot_motifs_medecine_generale_bis(activite_stats)
    print("Graphique généré : output/charts/motifs_medecine_bis.png")


    repartition_infirmiere_path = "data/processed/repartition_activite_infirmiere.csv"
    plot_repartition_activite_infirmiere(repartition_infirmiere_path)
    print("Graphique généré : output/charts/repartition_activite_infirmiere.png")

    delai_psy_path = "data/processed/delai_attente_psy.csv"
    plot_delai_attente_psy(delai_psy_path)
    print("Graphique généré : output/charts/delai_attente_psy.png")
    
    compare_path = "data/processed/activite_infirmiere_compare.csv"
    plot_activite_infirmiere_compare(compare_path)
    print("Graphique généré : output/charts/activite_infirmiere_compare.png")

    plot_repartition_activite_depuis_reel(df_activite)
    print("Graphique généré : output/charts/repartition_activite_reelle.png")


    
    sites = {
        "UA": 95,
        "Institut agro Rennes Angers": 11,
        "UCO": 11,
        "ESA": 8,
        "TALM": 7,
        "ENSAM": 7,
        "ETSCO": 2,
        "ISTOM": 2,
        "ARIFTS": 1,
        "IFORIS": 1,
    }

    plot_actions_par_site_lisible(sites)
    print("Graphique généré : output/charts/actions_par_site_lisible.png")


    
    plot_duree_suivi(df_activite)
    print("Graphique généré : output/charts/duree_suivi.png")


    
    # plot_origine_stagiaires_pssm(df_pssm)
    # print("Graphique généré : output/charts/origine_pssm.png")

    #### RAPPORT WORD ####
    print_section("Génération du rapport Word")
    from app.generate_report import main as generate_report
    generate_report()

if __name__ == "__main__":
    main()