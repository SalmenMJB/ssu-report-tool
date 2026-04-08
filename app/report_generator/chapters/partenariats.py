"""
Chapitres Diététique et Nutrition, Partenariats & Perspectives.
"""

from app.report_generator.document_builder import ReportBuilder


DIETETIQUE_INTRO_TEXT = (
    "Le SSU propose des consultations de diététique et de nutrition pour accompagner "
    "les étudiant·e·s dans l'adoption de bonnes habitudes alimentaires. Ces "
    "consultations s'adressent notamment aux étudiant·e·s présentant des troubles "
    "du comportement alimentaire ou souhaitant améliorer leur équilibre nutritionnel."
)

PARTENARIATS_INTRO_TEXT = (
    "Le SSU développe et entretient de nombreux partenariats avec des acteurs "
    "institutionnels, associatifs et de santé, à l'échelle locale, régionale "
    "et nationale. Ces partenariats permettent d'enrichir l'offre de soins et "
    "de prévention proposée aux étudiant·e·s."
)

PERSPECTIVES_TEXT = (
    "Pour l'année universitaire à venir, le SSU entend consolider ses actions "
    "existantes et développer de nouvelles initiatives en matière de prévention, "
    "d'accompagnement psychologique et de santé globale."
)


def build_dietetique_chapter(
    builder: ReportBuilder,
) -> None:
    """Construit le chapitre Diététique et Nutrition."""

    builder.add_chapter("Diététique et Nutrition", DIETETIQUE_INTRO_TEXT)

    builder.add_editable_comment_zone()


def build_partenariats_chapter(
    builder: ReportBuilder,
) -> None:
    """Construit le chapitre Partenariats & Perspectives."""

    builder.add_chapter("Partenariats & Perspectives", PARTENARIATS_INTRO_TEXT)

    builder.add_section("Partenariats")
    builder.add_editable_comment_zone()

    builder.add_section("Perspectives", PERSPECTIVES_TEXT)
    builder.add_editable_comment_zone()
