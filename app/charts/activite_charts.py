import os
import matplotlib.pyplot as plt


def plot_visites_vaccinations(activite_stats):
    os.makedirs("output/charts", exist_ok=True)

    # --- VISITES ---
    visites = activite_stats["visites_effectuees"]
    visites = visites[visites.index.notna()]

    plt.figure(figsize=(6, 6))
    plt.pie(
        visites.values,
        labels=visites.index.astype(str),
        autopct="%1.1f%%",
        colors=["#E74C3C", "#2ECC71"]
    )
    plt.title("Visites effectuées")
    plt.tight_layout()
    plt.savefig("output/charts/visites.png")
    plt.close()

    # --- VACCINATIONS ---
    vaccinations = activite_stats["vaccinations"]
    vaccinations = vaccinations[vaccinations.index.notna()]

    plt.figure(figsize=(6, 6))
    plt.pie(
        vaccinations.values,
        labels=vaccinations.index.astype(str),
        autopct="%1.1f%%",
        colors=["#E74C3C", "#2ECC71"]
    )
    plt.title("Vaccinations effectuées")
    plt.tight_layout()
    plt.savefig("output/charts/vaccinations.png")
    plt.close()


def plot_top_nationalites(activite_stats):
    data = activite_stats["top_nationalites"]

    # optionnel : enlever France si tu veux mieux voir l'international
    # data = data[data.index != "FRANCE"]

    data = data.head(10)
    labels = data.index.astype(str)
    values = data.values

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color="#4A90E2")

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

    plt.title("Top nationalités")
    plt.xlabel("Nationalité")
    plt.ylabel("Nombre d'étudiants")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/charts/top_nationalites.png")
    plt.close()


def plot_handicap(activite_stats):
    data = activite_stats["handicap"]

    # enlever les non renseignés
    data = data[data.index.notna()]
    data = data[data.index.astype(str).str.lower() != "nan"]

    data = data.head(10)

    labels = data.index.astype(str)
    values = data.values

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(11, 6))
    bars = plt.bar(labels, values, color="#9B59B6")

    # offset = max(values) * 0.02 if len(values) > 0 else 1

    # for bar in bars:
    #     height = bar.get_height()
    #     plt.text(
    #         bar.get_x() + bar.get_width() / 2,
    #         height + offset,
    #         str(int(height)),
    #         ha="center",
    #         va="bottom",
    #         fontsize=9
    #     )

    plt.title("Répartition des handicaps")
    plt.xlabel("Type de handicap")
    plt.ylabel("Nombre d'étudiants")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/charts/handicap.png")
    plt.close()