"""
Chapitres Psychologie et Psychiatrie / Santé mentale.
"""

from app.report_generator.document_builder import ReportBuilder


PSY_INTRO_TEXT = (
    "Le pôle psychologique du SSU propose des consultations de psychologie clinique "
    "aux étudiant·e·s rencontrant des difficultés d'ordre psychologique, émotionnel "
    "ou relationnel. L'accès aux soins psychologiques constitue une priorité du "
    "service."
)

PSYCHIATRIE_INTRO_TEXT = (
    "Le SSU propose également des consultations psychiatriques pour les étudiant·e·s "
    "nécessitant une prise en charge spécialisée. Ces consultations sont assurées "
    "par des praticiens hospitaliers en lien avec les équipes du CHU d'Angers."
)

SANTE_MENTALE_TEXT = (
    "La santé mentale et le bien-être des étudiant·e·s sont au cœur des missions du "
    "SSU. Le Dispositif Santé Psy Étudiant (DSPE), les ateliers de bien-être et les "
    "actions de prévention contribuent à améliorer le mieux-vivre étudiant."
)

DSPE_TEXT = (
    "Le Dispositif Santé Psy Étudiant (DSPE) permet aux étudiant·e·s de bénéficier "
    "de séances d'accompagnement psychologique auprès de psychologues libéraux "
    "conventionnés, sans avance de frais."
)


def build_psy_chapter(
    builder: ReportBuilder,
    activite_stats: dict,
) -> None:
    """Construit le chapitre Psychologie."""

    builder.add_chapter("Psychologie", PSY_INTRO_TEXT)

    builder.add_section("Problématiques rencontrées")
    builder.add_image(
        "output/charts/problematique_psy.png",
        caption="Principales problématiques rencontrées en psychologie",
    )

    builder.add_section("Délai d'attente")
    builder.add_image(
        "output/charts/delai_attente_psy.png",
        caption="Délai d'attente avant première consultation",
    )

    builder.add_section("Durée de suivi")
    builder.add_image(
        "output/charts/duree_suivi.png",
        caption="Durée de suivi en psychologie",
    )

    # Chiffres clés
    psy_indicators = {}
    if "consultations_psychologie" in activite_stats:
        psy_indicators["Consultations psychologie"] = int(
            activite_stats["consultations_psychologie"]
        )
    if psy_indicators:
        builder.add_key_indicators_table(psy_indicators, title="Chiffres clés – Psychologie")

    builder.add_editable_comment_zone()


def build_psychiatrie_chapter(
    builder: ReportBuilder,
    activite_stats: dict,
) -> None:
    """Construit le chapitre Psychiatrie."""

    builder.add_chapter("Psychiatrie", PSYCHIATRIE_INTRO_TEXT)

    psy_indicators = {}
    if "consultations_psychiatrie" in activite_stats:
        psy_indicators["Consultations psychiatrie"] = int(
            activite_stats["consultations_psychiatrie"]
        )
    if psy_indicators:
        builder.add_key_indicators_table(psy_indicators, title="Chiffres clés – Psychiatrie")

    builder.add_editable_comment_zone()


def build_sante_mentale_chapter(
    builder: ReportBuilder,
    pssm_stats: dict = None,
) -> None:
    """Construit le chapitre Santé mentale et bien-être (inclut PSSM)."""

    builder.add_chapter("Santé mentale et bien-être", SANTE_MENTALE_TEXT)

    builder.add_section("Dispositif Santé Psy Étudiant (DSPE)", DSPE_TEXT)

    from app.report_generator.chapters.pssm import build_pssm_section
    build_pssm_section(builder, pssm_stats or {})

    builder.add_editable_comment_zone()
