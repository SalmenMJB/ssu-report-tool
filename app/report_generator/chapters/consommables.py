"""
Chapitre Éducation à la santé – Consommables et actions de prévention.
"""

from app.report_generator.document_builder import ReportBuilder


INTRO_TEXT = (
    "Le SSU mène des actions de prévention et d'éducation à la santé sur l'ensemble "
    "des campus de l'Université d'Angers et des établissements conventionnés. "
    "Ces actions portent notamment sur la santé sexuelle, la consommation d'alcool "
    "et de substances, la nutrition et le bien-être."
)

BILAN_ACTIONS_TEXT = (
    "Le bilan des actions d'éducation sanitaire détaille les thèmes abordés "
    "et les établissements impliqués tout au long de l'année."
)

CONSOMMABLES_TEXT = (
    "La distribution de matériel de prévention (préservatifs, éthylotests, livrets "
    "d'information…) constitue un levier important de sensibilisation. "
    "Le graphique ci-dessous présente la répartition des consommables distribués."
)

ACTIONS_TEXT = (
    "Les actions de prévention sont organisées sur les différents campus et sites "
    "des établissements partenaires."
)


def build_consommables_chapter(
    builder: ReportBuilder,
    consommables_stats: dict,
    bilan_actions_stats: dict = None,
) -> None:
    """Construit le chapitre Éducation à la santé / Consommables."""

    if bilan_actions_stats is None:
        bilan_actions_stats = {}

    builder.add_chapter("Éducation à la santé", INTRO_TEXT)

    # --- Bilan des actions ---
    builder.add_section("Bilan des actions d'éducation sanitaire", BILAN_ACTIONS_TEXT)
    builder.add_image(
        "output/charts/bilan_actions_par_theme.png",
        caption="Actions par thème",
    )
    builder.add_image(
        "output/charts/actions_par_site_lisible.png",
        caption="Actions de prévention par site",
    )

    # --- Consommables distribués ---
    builder.add_section("Consommables distribués", CONSOMMABLES_TEXT)
    builder.add_image(
        "output/charts/consommables_bilan_actions.png",
        caption="Consommables distribués lors des actions",
    )

    # Chiffres clés avec flèches bleues
    if "nombre_actions" in bilan_actions_stats:
        builder.add_blue_arrow_paragraph(
            f"Actions d'éducation sanitaire : "
            f"{int(bilan_actions_stats['nombre_actions'])}"
        )

    if "total_participants" in bilan_actions_stats:
        builder.add_blue_arrow_paragraph(
            f"Participants touchés : "
            f"{int(bilan_actions_stats['total_participants'])}"
        )

    conso_indicators = {}
    if "nombre_actions" in bilan_actions_stats:
        conso_indicators["Nombre d'actions"] = int(bilan_actions_stats["nombre_actions"])
    if "total_participants" in bilan_actions_stats:
        conso_indicators["Participants touchés"] = int(bilan_actions_stats["total_participants"])
    for key in ("total_preservatifs_externes", "total_preservatifs_internes"):
        if key in bilan_actions_stats:
            label = key.replace("total_", "").replace("_", " ").capitalize()
            conso_indicators[label] = int(bilan_actions_stats[key])
    if "total_ethylo_0_5" in bilan_actions_stats:
        conso_indicators["Éthylotests 0,5‰"] = int(bilan_actions_stats["total_ethylo_0_5"])
    if "total_packs_arret_tabac" in bilan_actions_stats:
        conso_indicators["Packs arrêt tabac"] = int(bilan_actions_stats["total_packs_arret_tabac"])

    if conso_indicators:
        builder.add_key_indicators_table(
            conso_indicators, title="Chiffres clés – Prévention"
        )

    builder.add_editable_comment_zone()
