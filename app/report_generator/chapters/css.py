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
    css_stats: dict = None,
) -> None:
    """Construit le chapitre Centre de santé sexuelle."""

    if css_stats is None:
        css_stats = {}

    builder.add_chapter("Centre de santé sexuelle", INTRO_TEXT)

    builder.add_section("Activité du centre", ACTIVITE_TEXT)

    # Graphique des motifs réels CSS (si disponible)
    builder.add_image(
        "output/charts/motifs_reels_css.png",
        caption="Motifs réels au Centre de Santé Sexuelle",
    )

    # Chiffres clés avec flèches bleues
    css_total = css_stats.get(
        "total_consultations_css",
        activite_stats.get("consultations_css", None),
    )
    if css_total is not None:
        builder.add_blue_arrow_paragraph(
            f"Consultations centre de planification : {int(css_total)}"
        )

    css_indicators = {}
    if css_total is not None:
        css_indicators["Consultations centre de planification"] = int(css_total)
    if css_indicators:
        builder.add_key_indicators_table(
            css_indicators, title="Chiffres clés – Centre de santé sexuelle"
        )

    builder.add_editable_comment_zone()

