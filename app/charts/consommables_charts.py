import matplotlib.pyplot as plt

def plot_consommables(indicators):
    #garder uniquement les totaux
    data = {
        key.replace("total_", ""): value
        for key, value in indicators.items()
        if key.startswith("total_") and value > 0    
    }

    # trier 
    data = dict(sorted(data.items(), key=lambda x:x[1], reverse=True))

    labels = list(data.keys())
    labels = [label.replace("_", " ") for label in labels] # on les renomme pour le rapport
    values = list(data.values())

    plt.figure(figsize=(12,6))
    bars = plt.bar(labels, values, color="#2ECC71")
    # ajouter les valeurs
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            str(int(height)),
            ha='center',
            va='bottom'
        )
    plt.title("Consommables distribués")
    plt.xlabel("Type de matériel")
    plt.ylabel("Quantité")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.savefig("output/charts/consommables.png")
    plt.close()


def plot_actions_par_campus(indicators):
    data = indicators["actions_par_campus"]

    # enlever NaN
    data = data[data.index.notna()]

    labels = data.index.astype(str)
    values = data.values

    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, values, color="#16A085")

    #valeurs
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            str(int(height)),
            ha='center',
            va='bottom'
        )
    plt.title("Actions de prévention par campus")
    plt.xlabel("Campus")
    plt.ylabel("Nombre d'actions")

    plt.tight_layout()
    plt.savefig("output/charts/actions_par_campus.png")
    plt.close()