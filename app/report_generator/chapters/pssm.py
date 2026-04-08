"""
Chapitre PSSM – Premiers Secours en Santé Mentale.
Ce module expose build_pssm_section, qui insère le contenu PSSM comme une
section (Heading 2) à l'intérieur d'un chapitre existant (ex. Santé mentale).
"""

from app.report_generator.document_builder import ReportBuilder


INTRO_TEXT = (
    "Le SSU organise des formations aux Premiers Secours en Santé Mentale (PSSM). "
    "Ces formations sensibilisent les participants à identifier les signes de détresse "
    "psychologique et à orienter les personnes concernées vers les ressources "
    "adaptées."
)

SESSIONS_TEXT = (
    "Le nombre de sessions organisées et le profil des participant·e·s témoignent "
    "de l'engagement du SSU dans la promotion de la santé mentale sur le campus."
)


def build_pssm_section(
    builder: ReportBuilder,
    pssm_stats: dict,
) -> None:
    """
    Insère le contenu PSSM comme une section (Heading 2) dans le chapitre courant.
    À appeler depuis build_sante_mentale_chapter.
    """

    builder.add_section("Premiers Secours en Santé Mentale (PSSM)", INTRO_TEXT)
    builder.add_subsection("Sessions de formation", SESSIONS_TEXT)
    builder.add_image(
        "output/charts/pssm_sessions.png",
        caption="Sessions PSSM par année",
    )

    # Chiffres clés
    pssm_indicators = {}
    if "nombre_sessions" in pssm_stats:
        pssm_indicators["Nombre de sessions"] = int(pssm_stats["nombre_sessions"])
    if "total_etudiants_ua" in pssm_stats:
        pssm_indicators["Étudiant·e·s UA formé·e·s"] = int(pssm_stats["total_etudiants_ua"])
    if "total_etudiants_autres" in pssm_stats:
        pssm_indicators["Étudiant·e·s autres établissements"] = int(
            pssm_stats["total_etudiants_autres"]
        )
    if "total_personnels_ua" in pssm_stats:
        pssm_indicators["Personnels UA formé·e·s"] = int(pssm_stats["total_personnels_ua"])
    if "total_participants_declares" in pssm_stats:
        pssm_indicators["Total participants déclarés"] = int(
            pssm_stats["total_participants_declares"]
        )
    if pssm_indicators:
        builder.add_key_indicators_table(pssm_indicators, title="Chiffres clés – PSSM")


def build_pssm_chapter(
    builder: ReportBuilder,
    pssm_stats: dict,
) -> None:
    """
    Construit le chapitre PSSM complet (Heading 1).
    Alias de build_pssm_section pour une utilisation en chapitre autonome.
    """
    builder.add_chapter("Premiers Secours en Santé Mentale", INTRO_TEXT)
    build_pssm_section(builder, pssm_stats)
