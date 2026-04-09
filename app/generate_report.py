"""
Script d'intégration principal : génère le rapport Word SSU complet.

Usage :
    python -m app.generate_report

Le fichier Word est sauvegardé dans output/rapport_ssu_2024_2025.docx
"""

import os
import warnings

warnings.filterwarnings(
    "ignore",
    message="Workbook contains no default style, apply openpyxl's default",
)

from app.parsers.effectifs import parse_effectifs_file
from app.parsers.stats_standard import parse_stats_standard_file
from app.parsers.consommables import parse_consommables_file
from app.parsers.stat_activite import parse_stat_activite_file
from app.parsers.pssm import parse_pssm_file
from app.parsers.psy import parse_psy_file

from app.services.indicator_service import (
    compute_effectifs_indicators,
    compute_stats_standard_indicators,
    compute_consommables_indicators,
    compute_stat_activite_indicators,
    compute_pssm_indicators,
)

from app.report_generator.document_builder import ReportBuilder
from app.report_generator.chapters.intro import build_intro_chapter
from app.report_generator.chapters.effectifs import build_effectifs_chapter
from app.report_generator.chapters.medecine import build_medecine_chapter
from app.report_generator.chapters.ide import build_ide_chapter
from app.report_generator.chapters.consommables import build_consommables_chapter
from app.report_generator.chapters.dspe import (
    build_psy_chapter,
    build_psychiatrie_chapter,
    build_sante_mentale_chapter,
)
from app.report_generator.chapters.css import build_css_chapter
from app.report_generator.chapters.partenariats import (
    build_dietetique_chapter,
    build_partenariats_chapter,
)

OUTPUT_DOCX = "output/rapport_ssu_2024_2025.docx"
LOGO_PATH = "app/templates/assets/logo_ua.png"


def _load_data():
    """Charge et parse tous les fichiers de données disponibles."""
    data = {}

    activite_path = "data/raw/stat_activite.xlsx"
    if os.path.isfile(activite_path):
        data["df_activite"] = parse_stat_activite_file(activite_path)
        data["activite_stats"] = compute_stat_activite_indicators(data["df_activite"])
    else:
        data["df_activite"] = None
        data["activite_stats"] = {}

    effectifs_path = "data/raw/evolution_etab_conventionnes.xlsx"
    if os.path.isfile(effectifs_path):
        data["df_effectifs"] = parse_effectifs_file(effectifs_path)
        data["effectifs_stats"] = compute_effectifs_indicators(data["df_effectifs"])
    else:
        data["df_effectifs"] = None
        data["effectifs_stats"] = {}

    stats_path = "data/raw/stats_standard_ssu.xlsx"
    if os.path.isfile(stats_path):
        data["df_stats"] = parse_stats_standard_file(stats_path)
        data["stats_stats"] = compute_stats_standard_indicators(data["df_stats"])
    else:
        data["df_stats"] = None
        data["stats_stats"] = {}

    consommables_path = "data/raw/extraction_consommables_actions_24_25.xlsx"
    if os.path.isfile(consommables_path):
        data["df_consommables"] = parse_consommables_file(consommables_path)
        data["consommables_stats"] = compute_consommables_indicators(data["df_consommables"])
    else:
        data["df_consommables"] = None
        data["consommables_stats"] = {}

    pssm_path = "data/raw/recap_pssm.xlsx"
    if os.path.isfile(pssm_path):
        pssm_sheets = parse_pssm_file(pssm_path)
        data["pssm_stats"] = compute_pssm_indicators(pssm_sheets)
    else:
        data["pssm_stats"] = {}

    psy_path = "data/raw/stats_psy.xlsx"
    if os.path.isfile(psy_path):
        data["df_psy"] = parse_psy_file(psy_path)
    else:
        data["df_psy"] = None

    return data


def main():
    """Point d'entrée principal de la génération du rapport."""

    print("=" * 60)
    print("  Génération du rapport SSU 2024-2025")
    print("=" * 60)

    # 1. Chargement des données
    print("\n[1/3] Chargement des données...")
    data = _load_data()

    # 2. Construction du document Word
    print("[2/3] Construction du rapport Word...")
    os.makedirs("output", exist_ok=True)

    builder = ReportBuilder(OUTPUT_DOCX)

    # Page de titre
    builder.add_title_page(
        title="Rapport d'activité",
        subtitle="2024 – 2025",
        logo_path=LOGO_PATH,
    )

    # Table des matières
    builder.add_table_of_contents()

    # Chapitres dans l'ordre requis
    # 1. Présentation générale
    build_intro_chapter(builder, data["activite_stats"])

    # 2. Pôle administratif
    build_effectifs_chapter(
        builder,
        data["df_stats"],
        data["df_effectifs"],
        data["stats_stats"],
        data["effectifs_stats"],
    )

    # 3. Médecine générale
    build_medecine_chapter(builder, data["df_activite"], data["activite_stats"])

    # 4. Service infirmier
    build_ide_chapter(builder, data["activite_stats"])

    # 5. Éducation à la santé
    build_consommables_chapter(builder, data["consommables_stats"])

    # 6. Psychologie
    build_psy_chapter(builder, data["activite_stats"])

    # 7. Psychiatrie
    build_psychiatrie_chapter(builder, data["activite_stats"])

    # 8. Santé mentale et bien-être (inclut PSSM et DSPE)
    build_sante_mentale_chapter(builder, data["pssm_stats"])

    # 9. Centre de santé sexuelle
    build_css_chapter(builder, data["activite_stats"])

    # 10. Diététique et Nutrition
    build_dietetique_chapter(builder)

    # 11. Partenariats & Perspectives
    build_partenariats_chapter(builder)

    # 3. Sauvegarde
    print("[3/3] Sauvegarde...")
    builder.save()
    print("\n✅ Rapport généré avec succès !")
    print(f"   Fichier : {OUTPUT_DOCX}")
    print(
        "\n   ℹ️  Ouvrez le fichier dans Word ou LibreOffice et appuyez sur\n"
        "      F9 (Windows) / Cmd+A+F9 (Mac) pour mettre à jour le sommaire."
    )


if __name__ == "__main__":
    main()
