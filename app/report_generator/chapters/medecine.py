"""
Chapitre 3 – Médecine générale.
"""

from app.report_generator.document_builder import ReportBuilder


INTRO_TEXT = (
    "Le pôle médecine générale du SSU assure des consultations de médecine générale, "
    "des bilans de prévention, des consultations spécialisées et le suivi des "
    "étudiant·e·s en situation de handicap. Il représente le cœur de l'activité "
    "clinique du service."
)

MOTIFS_TEXT = (
    "L'analyse des motifs de consultation permet d'identifier les principales "
    "problématiques de santé rencontrées par les étudiant·e·s et d'adapter les "
    "réponses du service."
)

BILANS_TEXT = (
    "Les bilans de prévention sont proposés à l'ensemble des étudiant·e·s, "
    "notamment les primo-entrants et les étudiants internationaux."
)

AMENAGEMENTS_TEXT = (
    "Le SSU instruit les dossiers d'aménagement d'études pour les étudiant·e·s "
    "en situation de handicap ou de maladie chronique."
)


def build_medecine_chapter(
    builder: ReportBuilder,
    df_activite,
    activite_stats: dict,
) -> None:
    """Construit le chapitre Médecine générale."""

    builder.add_chapter("Médecine générale", INTRO_TEXT)

    # --- Activité médicale ---
    builder.add_section("Activité médicale")
    builder.add_image(
        "output/charts/evolution_activite_medicale.png",
        caption="Évolution de l'activité médicale",
    )
    builder.add_image(
        "output/charts/repartition_activite_medicale.png",
        caption="Répartition de l'activité médicale",
    )

    # Chiffres clés
    med_indicators = {}
    if "consultations_medecine_generale" in activite_stats:
        med_indicators["Consultations médecine générale"] = int(
            activite_stats["consultations_medecine_generale"]
        )
    if "consultations_bilans" in activite_stats:
        med_indicators["Bilans de prévention"] = int(activite_stats["consultations_bilans"])
    if med_indicators:
        builder.add_key_indicators_table(med_indicators, title="Chiffres clés – Médecine générale")

    # --- Motifs de consultation ---
    builder.add_section("Motifs de consultation", MOTIFS_TEXT)
    builder.add_image(
        "output/charts/top_motifs.png",
        caption="Top 10 des motifs de consultation",
    )
    builder.add_image(
        "output/charts/motifs_medecine_generale_charts.png",
        caption="Motifs de médecine générale",
    )
    builder.add_image(
        "output/charts/motifs_medecine_bis.png",
        caption="Motifs de consultation (détail)",
    )

    # --- Bilans de prévention ---
    builder.add_section("Bilans de prévention", BILANS_TEXT)
    builder.add_image(
        "output/charts/bilans_par_composante.png",
        caption="Bilans par composante",
    )
    builder.add_image(
        "output/charts/bilans_internationaux.png",
        caption="Bilans étudiants internationaux",
    )
    builder.add_image(
        "output/charts/bilans_par_filiere.png",
        caption="Bilans par filière",
    )

    # --- Aménagements ---
    builder.add_section("Aménagements d'études", AMENAGEMENTS_TEXT)
    builder.add_image(
        "output/charts/evolution_amenagements.png",
        caption="Évolution des aménagements",
    )
    builder.add_image(
        "output/charts/repartition_amenagements.png",
        caption="Répartition des aménagements",
    )

    builder.add_editable_comment_zone()
