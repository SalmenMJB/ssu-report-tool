import os
import matplotlib.pyplot as plt
import pandas as pd


def plot_actions_par_site_lisible(data):
    """
    data peut être :
    - un dict {"UA": 95, "UCO": 11, ...}
    - ou une Series pandas
    """

    if isinstance(data, dict):
        s = pd.Series(data)
    else:
        s = data.copy()

    s = s.sort_values(ascending=True)

    os.makedirs("output/charts", exist_ok=True)

    plt.figure(figsize=(10, 6))
    bars = plt.barh(s.index.astype(str), s.values)

    offset = max(s.values) * 0.01 if len(s.values) > 0 else 1

    for bar in bars:
        width = bar.get_width()
        plt.text(
            width + offset,
            bar.get_y() + bar.get_height() / 2,
            str(int(width)),
            va="center"
        )

    plt.title("Répartition des lieux et nombre d’actions par site")
    plt.xlabel("Nombre d’actions")
    plt.ylabel("Site")
    plt.tight_layout()
    plt.savefig("output/charts/actions_par_site_lisible.png")
    plt.close()