"""
Utilitaires pour le calcul de l'année académique courante.
"""

from datetime import date


def get_academic_year() -> tuple[int, int]:
    """
    Retourne l'année académique courante sous forme d'un tuple (year1, year2).

    La rentrée universitaire a lieu en septembre. Ainsi :
    - Si le mois actuel est >= 9 (septembre), l'année académique est (année, année+1).
    - Si le mois actuel est < 9, l'année académique est (année-1, année).

    Exemples :
        Avril 2026  → (2025, 2026)
        Octobre 2026 → (2026, 2027)
    """
    today = date.today()
    if today.month >= 9:
        year1 = today.year
        year2 = today.year + 1
    else:
        year1 = today.year - 1
        year2 = today.year
    return year1, year2


def get_academic_year_label(separator: str = "-") -> str:
    """
    Retourne l'étiquette de l'année académique courante.

    Exemples :
        get_academic_year_label()     → "2025-2026"
        get_academic_year_label(" – ") → "2025 – 2026"
    """
    year1, year2 = get_academic_year()
    return f"{year1}{separator}{year2}"
