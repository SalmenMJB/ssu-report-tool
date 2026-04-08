"""
Chapitre 4 – Service infirmier (IDE).
"""

from app.report_generator.document_builder import ReportBuilder


INTRO_TEXT = (
    "Le service infirmier du SSU assure les consultations infirmières, les soins "
    "courants, les vaccinations et le suivi des étudiants. Les infirmier·ère·s "
    "diplômé·e·s d'État (IDE) jouent un rôle essentiel dans la prise en charge "
    "quotidienne des étudiant·e·s."
)

ACTIVITE_TEXT = (
    "L'activité infirmière recouvre un large spectre d'actes : consultations libres, "
    "soins sur prescription, entretiens infirmiers, vaccinations et orientation "
    "vers les médecins ou spécialistes."
)

VACCINATIONS_TEXT = (
    "Les vaccinations constituent une part significative de l'activité infirmière. "
    "Le SSU propose une offre vaccinale diversifiée, notamment pour les primo-entrants."
)


def build_ide_chapter(
    builder: ReportBuilder,
    activite_stats: dict,
) -> None:
    """Construit le chapitre Service infirmier."""

    builder.add_chapter("Service infirmier", INTRO_TEXT)

    # --- Activité infirmière ---
    builder.add_section("Activité infirmière", ACTIVITE_TEXT)
    builder.add_image(
        "output/charts/repartition_activite_infirmiere.png",
        caption="Répartition de l'activité infirmière",
    )
    builder.add_image(
        "output/charts/activite_infirmiere_compare.png",
        caption="Comparaison de l'activité infirmière",
    )
    builder.add_image(
        "output/charts/repartition_activite_reelle.png",
        caption="Répartition de l'activité réelle",
    )

    # Chiffres clés avec flèches bleues
    if "consultations_ide" in activite_stats:
        builder.add_blue_arrow_paragraph(
            f"Consultations IDE : {int(activite_stats['consultations_ide'])}"
        )

    ide_indicators = {}
    if "consultations_ide" in activite_stats:
        ide_indicators["Consultations IDE"] = int(activite_stats["consultations_ide"])
    if ide_indicators:
        builder.add_key_indicators_table(ide_indicators, title="Chiffres clés – Service infirmier")

    # --- Visites et vaccinations ---
    builder.add_section("Visites et vaccinations", VACCINATIONS_TEXT)
    builder.add_image(
        "output/charts/visites.png",
        caption="Visites effectuées",
    )
    builder.add_image(
        "output/charts/vaccinations.png",
        caption="Vaccinations réalisées",
    )

    builder.add_editable_comment_zone()
