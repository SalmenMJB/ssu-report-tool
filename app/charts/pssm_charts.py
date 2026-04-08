import matplotlib.pyplot as plt


def plot_pssm_sessions(indicators):
    data = indicators["sessions_par_feuille"]

    labels = data.index.astype(str)
    values = data.values

    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color="#F39C12")  # orange

    # valeurs au-dessus
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            str(int(height)),
            ha='center',
            va='bottom'
        )

    plt.title("Nombre de sessions PSSM par année")
    plt.xlabel("Année / Feuille")
    plt.ylabel("Nombre de sessions")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.savefig("output/charts/pssm_sessions.png")
    plt.close()