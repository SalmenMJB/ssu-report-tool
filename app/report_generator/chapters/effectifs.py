"""
Chapitre 2 – Pôle administratif / Effectifs et activité administrative.
"""

from app.report_generator.document_builder import ReportBuilder


INTRO_TEXT = (
    "Le pôle administratif du SSU assure l'accueil, la prise en charge des appels "
    "téléphoniques et la gestion des dossiers étudiants. Il constitue le premier "
    "point de contact avec le service pour la majorité des étudiant·e·s."
)

APPELS_TEXT = (
    "Le standard téléphonique est un indicateur important de l'activité. "
    "Le graphique ci-dessous présente l'évolution des appels reçus par mois."
)

EFFECTIFS_TEXT = (
    "L'évolution des effectifs étudiants par établissement permet de mesurer "
    "la progression du service et son rayonnement territorial."
)


def build_effectifs_chapter(
    builder: ReportBuilder,
    df_stats,
    df_effectifs,
    stats_stats: dict,
    effectifs_stats: dict,
) -> None:
    """Construit le chapitre Pôle administratif."""

    builder.add_chapter("Pôle administratif", INTRO_TEXT)

    # --- Appels téléphoniques ---
    builder.add_section("Standard téléphonique", APPELS_TEXT)
    builder.add_image(
        "output/charts/appels_par_mois.png",
        caption="Appels reçus par mois",
    )

    # Chiffres clés appels avec flèches bleues
    if "total_appels_latest_year" in stats_stats:
        builder.add_blue_arrow_paragraph(
            f"Total appels : {int(stats_stats['total_appels_latest_year'])}"
        )
    if "latest_year" in stats_stats:
        latest_year_label = stats_stats["latest_year"]
        if latest_year_label.startswith("appels_"):
            latest_year_label = latest_year_label[len("appels_"):]
        builder.add_blue_arrow_paragraph(
            f"Année de référence : {latest_year_label}"
        )

    appels_indicators = {}
    if "total_appels_latest_year" in stats_stats:
        appels_indicators["Total appels"] = int(stats_stats["total_appels_latest_year"])
    if "latest_year" in stats_stats:
        appels_indicators["Année de référence"] = stats_stats["latest_year"].replace("appels_", "")
    if appels_indicators:
        builder.add_key_indicators_table(appels_indicators, title="Chiffres clés – Appels")

    # --- Effectifs ---
    builder.add_section("Évolution des effectifs étudiants", EFFECTIFS_TEXT)
    builder.add_image(
        "output/charts/evolution_effectifs.png",
        caption="Évolution des effectifs par établissement",
    )
    builder.add_image(
        "output/charts/top_etablissements.png",
        caption="Top établissements (dernière année)",
    )

    # Chiffres clés effectifs avec flèches bleues
    effectifs_indicators = {}
    for key, value in effectifs_stats.items():
        if key.startswith("total_") and "/" in key:
            year = key.replace("total_", "")
            effectifs_indicators[f"Effectifs {year}"] = int(value)
    if "latest_year_used" in effectifs_stats:
        effectifs_indicators["Dernière année utilisée"] = effectifs_stats["latest_year_used"]
    if effectifs_indicators:
        builder.add_key_indicators_table(effectifs_indicators, title="Chiffres clés – Effectifs")

    builder.add_editable_comment_zone()
