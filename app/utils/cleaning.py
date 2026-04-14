"""
Module de nettoyage et standardisation des données SSU.

Fournit des fonctions utilitaires pour normaliser les labels et les noms
d'établissements afin d'assurer une cohérence dans toutes les analyses.
"""

import re
import unicodedata


def normalize_text(value) -> str:
    """
    Normalise une valeur texte : supprime les espaces superflus,
    met en minuscules et retire les accents.

    Retourne une chaîne vide si la valeur est None ou NaN.
    """
    if value is None:
        return ""
    text = str(value)
    # Supprimer les espaces en début/fin et réduire les espaces multiples
    text = re.sub(r"\s+", " ", text).strip()
    # Normaliser les caractères Unicode (NFD puis suppression des diacritiques)
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return text.lower()


def standardize_simple_labels(series):
    """
    Standardise les étiquettes d'une Series pandas :
    - Supprime les espaces en début/fin
    - Réduit les espaces multiples internes à un seul espace
    - Met la première lettre en majuscule (titre de phrase)

    Retourne une Series avec les valeurs nettoyées.
    """
    return (
        series.astype(str)
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
        .str.capitalize()
    )


# Correspondances vers les noms canoniques d'établissements
_ETABLISSEMENT_MAP = {
    # Université d'Angers
    "universite d angers": "UA",
    "université d'angers": "UA",
    "universite d'angers": "UA",
    "ua": "UA",
    "univ angers": "UA",
    # UCO
    "uco": "UCO",
    "universite catholique de l ouest": "UCO",
    "université catholique de l'ouest": "UCO",
    "catholique": "UCO",
    # ESA
    "esa": "ESA",
    "ecole superieure d agriculture": "ESA",
    "école supérieure d'agriculture": "ESA",
    # Institut Agro
    "institut agro": "Institut Agro",
    "institut agro rennes angers": "Institut Agro",
    "agro": "Institut Agro",
    # TALM
    "talm": "TALM",
    # ENSAM
    "ensam": "ENSAM",
    "arts et metiers": "ENSAM",
    "arts et métiers": "ENSAM",
    # ETSCO
    "etsco": "ETSCO",
    # ISTOM
    "istom": "ISTOM",
    # ARIFTS
    "arifts": "ARIFTS",
    # IFORIS
    "iforis": "IFORIS",
}


def standardize_etablissement(value) -> str:
    """
    Mappe un nom d'établissement brut vers sa forme standard canonique.

    Retourne la forme canonique si une correspondance est trouvée,
    sinon retourne la valeur originale nettoyée (strip + capitalize).
    """
    if value is None:
        return ""
    raw = str(value).strip()
    key = normalize_text(raw)
    canonical = _ETABLISSEMENT_MAP.get(key)
    if canonical:
        return canonical
    # Vérifier les correspondances partielles (la clé est contenue dans la valeur)
    for pattern, canonical_name in _ETABLISSEMENT_MAP.items():
        if pattern in key:
            return canonical_name
    # Aucune correspondance : retourner la valeur nettoyée
    return raw.capitalize() if raw else ""
