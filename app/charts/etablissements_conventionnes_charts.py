#from docx import Document
# import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from app.parsers.effectifs import parse_effectifs_file


def plot_etablissements_conventionnes():
    csv_path = "data/raw/evolution_etab_conventionnes.xlsx" # adapter le chemin si besoin
    df = parse_effectifs_file(csv_path)

    labels = df["etablissement"]
    somme = df["2025/2026"].sum()
    pourcentages = []
    for val in df["2025/2026"]:
        calcul = (val/somme)*100
        pourcentages.append(round(calcul,2))

    couleurs = {"#006400", # vert foncé,
                "#008000", # vert
                "#6B8E23", # vert jaunâtre
                "#9ACD32", # jaune-vert
                "#003b9b", # jaune
                "#FFA500", # orange
                "#FF8C00", # orange foncé
                "#CD853F", # brun foncé
                "#8B4513" # marron
                }

    fig, ax = plt.subplots(figsize=(12, 8))

    wedges, _ = ax.pie(
        pourcentages,
        colors=couleurs,
        startangle=85, # pour une orientation proche de la photo
        counterclock=False,
        wedgeprops=dict(edgecolor="white", linewidth=1.2)
    )

    ax.set(aspect="equal")

    for wedge, cat, pct in zip(wedges, labels, pourcentages):
        angle = (wedge.theta2 + wedge.theta1) / 2
        x = np.cos(np.deg2rad(angle))
        y = np.sin(np.deg2rad(angle))

        # position du texte à l'extérieur
        label_x = 1.28 * x
        label_y = 1.28 * y

        ha = "left" if x >= 0 else "right"

        ax.annotate(
            f"{cat}\n{pct:.0f}%",
            xy=(x, y),
            xytext=(label_x, label_y),
            ha=ha,
            va="center",
            fontsize=12,
            bbox=dict(boxstyle="square,pad=0.35", fc="white", ec="#bfbfbf", lw=1),
            arrowprops=dict(arrowstyle="-", color="#9e9e9e", lw=1.2, shrinkA=0, shrinkB=0)
        )

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_edgecolor("#d9d9d9")
        spine.set_linewidth(1)

    plt.tight_layout()


    plt.savefig("output/charts/etablissements_conventionnes.png", dpi=300, bbox_inches="tight")
    #plt.show()
