import os
import matplotlib.pyplot as plt


def plot_recap_consultations(activite_stats):
    motif_counts = activite_stats["top_motifs"]

    # mapping intelligent
    data = {
        "Médecine": motif_counts.get("Consultations médecine générale", 0),
        "Psychologie": motif_counts.get("Psychologie", 0),
        "Psychiatrie": motif_counts.get("Psychiatrie", 0),
        "IDE": motif_counts.get("Consultations IDE", 0),
        "CSS": motif_counts.get("Centre de planification", 0),
    }

    # debug 
    # print("DATA CAMEMBERT :", data)

    # enlever les 0
    data = {k: v for k, v in data.items() if v > 0}

    labels = list(data.keys())
    values = list(data.values())

    import os
    import matplotlib.pyplot as plt

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(7, 7))

    def autopct_format(values):
        def inner(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return f"{val}\n({pct:.1f}%)"
        return inner

    if len(values) > 0:
        plt.pie(
            values,
            labels=labels,
            autopct=autopct_format(values),
            colors=["#3498DB", "#9B59B6", "#E67E22", "#2ECC71", "#E74C3C"]
        )

    plt.title("Répartition des consultations")
    plt.tight_layout()
    plt.savefig("output/charts/recap_consultations.png")
    plt.close()