import os
import matplotlib.pyplot as plt

# On fait d’abord une version propre du graphique avec ces valeurs.
# Ensuite, plus tard, on branchera ça sur une vraie source Excel si vous l’avez.


"""
Pour l’instant, ce graphe est basé sur les valeurs vues dans l’ancien rapport.
Donc c’est une version template.

Plus tard, on pourra le rendre dynamique si vous récupérez :

un export Calcium,
ou un Excel historique des aménagements,
ou une table de suivi annuelle.
"""

def plot_evolution_amenagements():
    years = [
        "2014-2015",
        "2015-2016",
        "2016-2017",
        "2017-2018",
        "2018-2019",
        "2019-2020",
        "2020-2021",
        "2021-2022",
        "2022-2023",
        "2023-2024",
        "2024-2025",
    ]

    values = [247, 260, 352, 340, 465, 517, 529, 684, 753, 810, 995]

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(11, 6))
    plt.plot(years, values, marker="o")

    offset = max(values) * 0.01

    for x, y in zip(years, values):
        plt.text(x, y + offset, str(y), ha="center", va="bottom", fontsize=9)

    plt.title("Étudiants bénéficiant d'aménagements des conditions d'examen et/ou d'études")
    plt.xlabel("Année universitaire")
    plt.ylabel("Nombre d'étudiants")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/charts/evolution_amenagements.png")
    plt.close()