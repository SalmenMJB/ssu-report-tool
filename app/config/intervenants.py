"""
Configuration des intervenants du SSU.

Liste des médecins et infirmières permettant de catégoriser
les bilans de prévention par profession.
"""

# Noms des médecins (formes canoniques, insensibles à la casse lors de la comparaison)
MEDECINS = [
    "Dr Martin",
    "Dr Dupont",
    "Dr Bernard",
    "Dr Leroy",
    "Dr Moreau",
    "Dr Simon",
    "Dr Laurent",
    "Dr Lefebvre",
    "Dr Michel",
    "Dr Garcia",
]

# Noms des infirmières / infirmiers
INFIRMIERES = [
    "Inf. Durand",
    "Inf. Petit",
    "Inf. Robert",
    "Inf. Richard",
    "Inf. Thomas",
    "Inf. Blanc",
    "Inf. Fontaine",
    "Inf. Henry",
    "Inf. Rousseau",
    "Inf. Vincent",
]


def get_profession(intervenant: str) -> str:
    """
    Retourne la profession ('Médecin', 'Infirmier/Infirmière' ou 'Autre')
    en fonction du nom de l'intervenant.
    """
    if intervenant is None:
        return "Autre"
    name_lower = str(intervenant).lower()
    for medecin in MEDECINS:
        if medecin.lower() in name_lower:
            return "Médecin"
    for infirmiere in INFIRMIERES:
        if infirmiere.lower() in name_lower:
            return "Infirmier/Infirmière"
    # Détection générique par préfixe
    if name_lower.startswith("dr") or name_lower.startswith("dr."):
        return "Médecin"
    if name_lower.startswith("inf") or "infirm" in name_lower:
        return "Infirmier/Infirmière"
    return "Autre"
