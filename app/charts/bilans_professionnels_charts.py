import os
import matplotlib.pyplot as plt


def plot_bilans_par_profession(bilans_professionnels_indicators: dict) -> None:
    """
    Graphique en camembert comparant le nombre de bilans réalisés
    par les médecins versus les infirmières.
    """
    data = bilans_professionnels_indicators.get("bilans_par_profession")
    if data is None or len(data) == 0:
        return

    data = data[data.index.notna()]
    labels = data.index.astype(str)
    values = data.values

    colors = ["#3498DB", "#E74C3C", "#2ECC71", "#F39C12", "#9B59B6"]

    os.makedirs("output/charts", exist_ok=True)

    fig, ax = plt.subplots(figsize=(7, 7))

    def autopct_format(vals):
        def inner(pct):
            total = sum(vals)
            val = int(round(pct * total / 100.0))
            return f"{val}\n({pct:.1f}%)"
        return inner

    ax.pie(
        values,
        labels=labels,
        autopct=autopct_format(values),
        colors=colors[: len(values)],
        startangle=90,
    )

    ax.set_title("Bilans de prévention par profession")
    plt.tight_layout()
    plt.savefig("output/charts/bilans_par_profession.png")
    plt.close()


def plot_bilans_medecins_vs_infirmieres(bilans_professionnels_indicators: dict) -> None:
    """
    Graphique en barres comparant les bilans réalisés par les médecins
    et les infirmières.
    """
    data = bilans_professionnels_indicators.get("bilans_par_profession")
    if data is None or len(data) == 0:
        return

    data = data[data.index.notna()]

    os.makedirs("output/charts", exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 5))
    bar_colors = ["#3498DB" if "edecin" in str(label) else "#E74C3C"
                  for label in data.index]
    bars = ax.bar(data.index.astype(str), data.values, color=bar_colors)

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
