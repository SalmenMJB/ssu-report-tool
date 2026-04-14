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

CONSOMMABLES_TEXT = (
    "La distribution de matériel de prévention (préservatifs, éthylotests, livrets "
    "d'information…) constitue un levier important de sensibilisation. "
    "Le graphique ci-dessous présente la répartition des consommables distribués."
)

ACTIONS_TEXT = (
    "Les actions de prévention sont organisées sur les différents campus et sites "
    "des établissements partenaires."
)

BILAN_ACTIONS_TEXT = (
    "Le bilan des actions d'éducation sanitaire détaille les thèmes abordés "
    "et les établissements impliqués tout au long de l'année."
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

    # --- Consommables ---
    builder.add_section("Consommables distribués", CONSOMMABLES_TEXT)
    builder.add_image(
        "output/charts/consommables.png",
        caption="Consommables distribués",
    )

    # --- Actions par campus ---
    builder.add_section("Actions par campus", ACTIONS_TEXT)
    builder.add_image(
        "output/charts/actions_par_campus.png",
        caption="Actions de prévention par campus",
    )
    builder.add_image(
        "output/charts/actions_par_site_lisible.png",
        caption="Actions de prévention par site",
    )

    # --- Bilan des actions (nouveaux graphiques) ---
    builder.add_section("Bilan des actions d'éducation sanitaire", BILAN_ACTIONS_TEXT)
    builder.add_image(
        "output/charts/bilan_actions_par_theme.png",
        caption="Actions par thème",
    )
    builder.add_image(
        "output/charts/bilan_actions_par_campus.png",
        caption="Actions par campus (bilan)",
    )

    # Chiffres clés avec flèches bleues
    if "nombres_actions" in consommables_stats:
        builder.add_blue_arrow_paragraph(
            f"Nombre d'actions de prévention : "
            f"{int(consommables_stats['nombres_actions'])}"
        )

    if "nombre_actions" in bilan_actions_stats:
        builder.add_blue_arrow_paragraph(
            f"Actions d'éducation sanitaire (bilan) : "
            f"{int(bilan_actions_stats['nombre_actions'])}"
        )

    total_preservatifs = sum(
        int(consommables_stats.get(f"total_{k}", 0))
        for k in [
            "preservatifs_externes",
            "preservatifs_banane",
            "preservatifs_fraise",
            "preservatifs_sans_latex",
            "preservatifs_internes",
        ]
    )
    if total_preservatifs:
        builder.add_blue_arrow_paragraph(
            f"Préservatifs distribués : {total_preservatifs}"
        )

    conso_indicators = {}
    if "nombres_actions" in consommables_stats:
        conso_indicators["Nombre d'actions de prévention"] = int(
            consommables_stats["nombres_actions"]
        )
    if total_preservatifs:
        conso_indicators["Préservatifs distribués"] = total_preservatifs
    if "total_ethylo_0_5" in consommables_stats:
        conso_indicators["Éthylotests 0,5‰ distribués"] = int(
            consommables_stats["total_ethylo_0_5"]
        )
    if "total_packs_arret_tabac" in consommables_stats:
        conso_indicators["Packs arrêt tabac distribués"] = int(
            consommables_stats["total_packs_arret_tabac"]
        )

    if conso_indicators:
        builder.add_key_indicators_table(
            conso_indicators, title="Chiffres clés – Prévention"
        )

    builder.add_editable_comment_zone()
