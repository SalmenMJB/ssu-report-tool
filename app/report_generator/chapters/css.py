"""
Chapitre Centre de santé sexuelle (CSS).
"""

from app.report_generator.document_builder import ReportBuilder


INTRO_TEXT = (
    "Le Centre de santé sexuelle (CSS) du SSU propose des consultations de "
    "gynécologie, de contraception et de dépistage des infections sexuellement "
    "transmissibles (IST). Il contribue à la promotion de la santé sexuelle "
    "et reproductive des étudiant·e·s."
)

ACTIVITE_TEXT = (
    "L'activité du CSS recouvre les consultations de contraception, le dépistage "
    "des IST, les frottis cervico-utérins et les consultations de gynécologie générale."
)


def build_css_chapter(
    builder: ReportBuilder,
    activite_stats: dict,
) -> None:
    """Construit le chapitre Centre de santé sexuelle."""

    builder.add_chapter("Centre de santé sexuelle", INTRO_TEXT)

    builder.add_section("Activité du centre", ACTIVITE_TEXT)

    # Chiffres clés avec flèches bleues
    if "consultations_css" in activite_stats:
        builder.add_blue_arrow_paragraph(
            f"Consultations centre de planification : "
            f"{int(activite_stats['consultations_css'])}"
        )

    css_indicators = {}
    if "consultations_css" in activite_stats:
        css_indicators["Consultations centre de planification"] = int(
            activite_stats["consultations_css"]
        )
    if css_indicators:
        builder.add_key_indicators_table(
            css_indicators, title="Chiffres clés – Centre de santé sexuelle"
        )

    builder.add_editable_comment_zone()
