import os
import matplotlib.pyplot as plt


def plot_motifs_reels_css(css_indicators: dict) -> None:
    """
    Trace un graphique en barres horizontales des motifs réels
    au Centre de Santé Sexuelle (CSS).
    """
    motifs = css_indicators.get("motifs_reels_css")
    if motifs is None or len(motifs) == 0:
        return

    motifs = motifs[motifs.index.notna()].head(15)
    motifs = motifs.sort_values(ascending=True)

    os.makedirs("output/charts", exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, max(5, len(motifs) * 0.5)))
    bars = ax.barh(motifs.index.astype(str), motifs.values, color="#E74C3C")

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

    ax.set_title("Motifs réels au Centre de Santé Sexuelle")
    ax.set_xlabel("Nombre de consultations")
    ax.set_ylabel("Motif")
    plt.tight_layout()
    plt.savefig("output/charts/motifs_reels_css.png")
    plt.close()
