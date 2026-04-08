import os
import matplotlib.pyplot as plt


def plot_motifs_medecine_generale_bis(activite_stats):
    data = {
        "Médecine générale": activite_stats.get("consultations_medecine_generale", 0),
        "Santé mentale": activite_stats.get("consultations_psychologie", 0) + activite_stats.get("consultations_psychiatrie", 0),
        "Aménagement": activite_stats.get("consultations_css", 0),
        "Bilans": activite_stats["top_motifs"].get("Bilan de prévention", 0),
    }

    data = {k: v for k, v in data.items() if v > 0}

    labels = list(data.keys())
    values = list(data.values())


    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(7, 7))

    def autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100))
        return f"{val}\n({pct:.1f}%)"

    plt.pie(values, labels=labels, autopct=autopct)

    plt.title("Motifs des consultations médicales")
    plt.savefig("output/charts/motifs_medecine_bis.png")
    plt.close()