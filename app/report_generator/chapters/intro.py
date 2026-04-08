"""
Chapitre 1 – Présentation générale du service.
"""

from app.report_generator.document_builder import ReportBuilder


INTRO_TEXT = (
    "Le Service de Santé Universitaire (SSU) de l'Université d'Angers assure la "
    "promotion de la santé, la prévention et les soins pour l'ensemble des "
    "étudiant·e·s. Agréé Centre de Santé depuis le 26 mars 2012, il accueille les "
    "étudiant·e·s de l'Université d'Angers et des établissements conventionnés."
)

EFFECTIFS_TEXT = (
    "Le SSU prend en charge les étudiant·e·s inscrits à l'UA ainsi que ceux des "
    "écoles conventionnées. L'évolution des effectifs inscrits est présentée "
    "ci-dessous."
)


def build_intro_chapter(
    builder: ReportBuilder,
    activite_stats: dict,
) -> None:
    """Construit le chapitre Présentation générale du service."""

    builder.add_chapter("Présentation générale du service", INTRO_TEXT)

    # --- Récapitulatif consultations ---
    builder.add_section("Récapitulatif et évolution des consultations")
    builder.add_image(
        "output/charts/recap_consultations.png",
        caption="Récapitulatif des consultations",
    )
    builder.add_image(
        "output/charts/consultations_par_centre.png",
        caption="Consultations par centre",
    )

    # Chiffres clés
    indicators = {}
    if "total_consultations" in activite_stats:
        indicators["Total consultations"] = int(activite_stats["total_consultations"])
    if "etudiants_uniques" in activite_stats:
        indicators["Étudiant·e·s uniques"] = int(activite_stats["etudiants_uniques"])
    if "age_moyen" in activite_stats:
        indicators["Âge moyen"] = f"{activite_stats['age_moyen']:.1f} ans"
    if indicators:
        builder.add_key_indicators_table(indicators, title="Chiffres clés – Activité globale")

    # --- Répartition par sexe ---
    builder.add_section("Répartition par sexe")
    builder.add_image(
        "output/charts/repartition_sexe.png",
        caption="Répartition par sexe",
    )

    # --- Nationalités ---
    builder.add_section("Nationalités")
    builder.add_image(
        "output/charts/top_nationalites.png",
        caption="Principales nationalités",
    )

    # --- Handicap ---
    builder.add_section("Handicap")
    builder.add_image(
        "output/charts/handicap.png",
        caption="Répartition des situations de handicap",
    )

    # --- Effectifs établissements conventionnés ---
    builder.add_section("Effectifs et établissements conventionnés", EFFECTIFS_TEXT)
    builder.add_image(
        "output/charts/etablissements_conventionnes.png",
        caption="Établissements conventionnés",
    )

    builder.add_editable_comment_zone()
