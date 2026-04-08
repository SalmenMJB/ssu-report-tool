import os
import matplotlib.pyplot as plt


def plot_consultations_par_centre(activite_stats):
    data = activite_stats["consultations_par_centre"]

    labels = data.index.astype(str)
    values = data.values

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color="#2980B9")

    offset = max(values) * 0.02 if len(values) > 0 else 1

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + offset,
            str(int(height)),
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.title("Consultations par centre")
    plt.xlabel("Centre")
    plt.ylabel("Nombre de consultations")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig("output/charts/consultations_par_centre.png")
    plt.close()


def plot_top_motifs(activite_stats):
    data = activite_stats["top_motifs"].head(10)

    labels = data.index.astype(str)
    values = data.values

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(11, 6))
    bars = plt.bar(labels, values, color="#E67E22")

    offset = max(values) * 0.02 if len(values) > 0 else 1

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + offset,
            str(int(height)),
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.title("Top motifs de consultation")
    plt.xlabel("Motif")
    plt.ylabel("Nombre de consultations")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig("output/charts/top_motifs.png")
    plt.close()


def plot_repartition_sexe(activite_stats):
    data = activite_stats["repartition_sexe"]
    data = data[data.index.notna()]

    labels = data.index.astype(str)
    values = data.values

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(7, 7))

    def autopct_format(values):
        def inner(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return f"{val}\n({pct:.1f}%)"
        return inner

    plt.pie(
        values,
        labels=labels,
        autopct=autopct_format(values),
        colors=["#FF69B4", "#4A90E2"]
    )

    plt.title("Répartition par sexe")
    plt.tight_layout()
    plt.savefig("output/charts/repartition_sexe.png")
    plt.close()