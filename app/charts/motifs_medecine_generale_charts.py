import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_motifs_medecine_generale_charts(df):
    df_motifs = df[df["motif"]=="Consultations médecine générale"]
    motifs_reels = df_motifs["motif réels"].drop_duplicates()
    # print(motifs_reels)

    ### Aménagements ###
    amenagement_regex = r'(?i).*aménagement.*'
    df_amenagements = df_motifs[df_motifs["motif réels"].str.contains(amenagement_regex,na=False)]
    nb_amenagements = df_amenagements.shape[0]
    df_amenagements_total = pd.DataFrame({"motif réels" : ["Aménagement d'études supérieures"],
                                        "Nombre par motif" : [nb_amenagements]})
    
    
    ### Bilan de santé ###
    bilan_regex = r'(?i).*bilan de santé.*'
    df_bilan = df_motifs[df_motifs["motif réels"].str.contains(bilan_regex,na=False)]
    nb_bilan = df_bilan.shape[0]
    df_bilan_total = pd.DataFrame({"motif réels" : ["Bilan de santé préventifs"],
                                        "Nombre par motif" : [nb_bilan]})


    ### Santé mentale ###
    sante_mentale_regex = r'(?i)(.*(première écoute|suivi santé mentale).*)'
    df_sante_mentale = df_motifs[df_motifs["motif réels"].str.contains(sante_mentale_regex,na=False)]
    nb_sante_mentale = df_sante_mentale.shape[0]
    df_sante_mentale_total = pd.DataFrame({"motif réels" : ["Santé mentale"],
                                        "Nombre par motif" : [nb_sante_mentale]})


    ### Médecine générale ###
    medecine_generale_regex = r'(?i)(?:(?:^|;)(consultation)(?:;|$))|.*?(médecine générale|autre|urgence).*?'
    df_medecine_generale = df_motifs[df_motifs["motif réels"].str.contains(medecine_generale_regex,na=False)]
    nb_medecine_generale = df_medecine_generale.shape[0]
    df_medecine_generale_total = pd.DataFrame({"motif réels" : ["Médecine générale"],
                                        "Nombre par motif" : [nb_medecine_generale]})

    df_total = pd.concat([df_amenagements_total,df_bilan_total,df_sante_mentale_total,df_medecine_generale_total],ignore_index=True)
    # print(df_total)

    somme = df_total["Nombre par motif"].sum()
    pourcentages = []
    for val in df_total["Nombre par motif"]:
        calcul = (val/somme)*100
        pourcentages.append(round(calcul,2))

    fig, ax = plt.subplots(figsize=(12, 8))

    couleurs = {"#9E9E9E", #gris foncé
                "#4FC3F7", #bleu clair
                "#FF7043", #orange
                "#FF9800", #jaune
                }
    
    wedges, _ = ax.pie(
        pourcentages,
        colors=couleurs,
        startangle=85, # pour une orientation proche de la photo
        counterclock=False,
        wedgeprops=dict(edgecolor="white", linewidth=1.2)
    )

    ax.set(aspect="equal")

    for wedge, cat, pct in zip(wedges, df_total["motif réels"], pourcentages):
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


    plt.savefig("output/charts/motifs_medecine_generale_charts.png", dpi=300, bbox_inches="tight")
    # plt.show()