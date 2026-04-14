import os
import matplotlib.pyplot as plt


def plot_stat_gyneco(css_indicators: dict) -> None:
    """
    Graphique en barres des statistiques de gynécologie / centre de santé sexuelle.
    Affiche la répartition des motifs de consultation au CSS.
    """
    motifs = css_indicators.get("motifs_reels_css")
    if motifs is None or len(motifs) == 0:
        return

    motifs = motifs[motifs.index.notna()].head(10)
    motifs = motifs.sort_values(ascending=True)

    os.makedirs("output/charts", exist_ok=True)

    colors = [
        "#E74C3C",
        "#C0392B",
        "#E67E22",
        "#D35400",
        "#F39C12",
        "#F1C40F",
        "#2ECC71",
        "#27AE60",
        "#3498DB",
        "#2980B9",
    ]

    fig, ax = plt.subplots(figsize=(10, max(5, len(motifs) * 0.6)))
    bars = ax.barh(
        motifs.index.astype(str),
        motifs.values,
        color=colors[: len(motifs)],
    )

    offset = max(motifs.values) * 0.01 if len(motifs.values) > 0 else 1
    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + offset,
            bar.get_y() + bar.get_height() / 2,
            str(int(width)),
            va="center",
            fontsize=9,
        )

    ax.set_title("Statistiques gynécologie / Centre de Santé Sexuelle")
    ax.set_xlabel("Nombre de consultations")
    ax.set_ylabel("Motif")
    plt.tight_layout()
    plt.savefig("output/charts/stat_gyneco.png")
    plt.close()
