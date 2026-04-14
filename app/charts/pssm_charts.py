import os
import matplotlib.pyplot as plt


def plot_pssm_sessions(indicators):
    data = indicators["sessions_par_feuille"]

    labels = data.index.astype(str)
    values = data.values

    os.makedirs("output/charts", exist_ok=True)

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


def plot_pssm_lastest_year(pssm_stats: dict) -> None:
    """
    Graphique des participants PSSM pour la dernière année :
    étudiants UA, étudiants autres, personnels UA, personnels autres.
    """
    categories = {
        "Étudiants UA": pssm_stats.get("total_etudiants_ua", 0),
        "Étudiants autres": pssm_stats.get("total_etudiants_autres", 0),
        "Personnels UA": pssm_stats.get("total_personnels_ua", 0),
        "Personnels autres": pssm_stats.get("total_personnels_autres", 0),
    }
    categories = {k: int(v) for k, v in categories.items() if v and v > 0}

    if not categories:
        return

    os.makedirs("output/charts", exist_ok=True)

    colors = ["#F39C12", "#E67E22", "#3498DB", "#2980B9"]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(
        list(categories.keys()),
        list(categories.values()),
        color=colors[: len(categories)],
    )

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            str(int(height)),
            ha="center",
            va="bottom",
        )

    ax.set_title("Participants aux formations PSSM")
    ax.set_ylabel("Nombre de participants")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig("output/charts/pssm_latest_year.png")
    plt.close()