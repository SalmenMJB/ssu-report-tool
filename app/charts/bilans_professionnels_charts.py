import os
import matplotlib.pyplot as plt


def plot_bilans_medecins_vs_infirmieres(bilans_professionnels_indicators: dict) -> None:
    """
    Graphique en barres comparant le nombre de bilans réalisés
    par les médecins, les infirmières, et les autres intervenants.
    """
    medecins = bilans_professionnels_indicators.get("bilans_medecins", 0)
    infirmieres = bilans_professionnels_indicators.get("bilans_infirmieres", 0)
    autres = bilans_professionnels_indicators.get("bilans_autres_intervenants", 0)

    categories = {
        "Médecins": medecins,
        "Infirmier(e)s": infirmieres,
        "Autres": autres,
    }
    categories = {k: int(v) for k, v in categories.items() if v and v > 0}

    if not categories:
        return

    os.makedirs("output/charts", exist_ok=True)

    color_map = {
        "Médecins": "#3498DB",
        "Infirmier(e)s": "#E74C3C",
        "Autres": "#2ECC71",
    }
    bar_colors = [color_map.get(k, "#9B59B6") for k in categories]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(list(categories.keys()), list(categories.values()), color=bar_colors)

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            str(int(height)),
            ha="center",
            va="bottom",
            fontsize=10,
        )

    ax.set_title("Bilans de prévention : médecins vs infirmières")
    ax.set_xlabel("Profession")
    ax.set_ylabel("Nombre de bilans")
    plt.tight_layout()
    plt.savefig("output/charts/bilans_medecins_vs_infirmieres.png")
    plt.close()
