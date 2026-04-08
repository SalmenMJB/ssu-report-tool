"""
Styles et constantes visuelles pour le rapport SSU - Université d'Angers.
Les couleurs principales sont le bleu ciel et le noir, conformément à la charte
graphique de l'Université d'Angers.
"""

from docx.shared import Pt, Cm, RGBColor

# ---------------------------------------------------------------------------
# Couleurs
# ---------------------------------------------------------------------------

# Bleu ciel UA (Heading 1 du document de référence : 0ABBEF)
COLOR_BLUE = RGBColor(0x0A, 0xBB, 0xEF)

# Bleu ciel secondaire (Heading 2/3 du document de référence : 00B0F0)
COLOR_BLUE_LIGHT = RGBColor(0x00, 0xB0, 0xF0)

COLOR_BLACK = RGBColor(0x00, 0x00, 0x00)
COLOR_WHITE = RGBColor(0xFF, 0xFF, 0xFF)

# Bleu foncé pour en-tête de tableaux
COLOR_TABLE_HEADER = RGBColor(0x0A, 0xBB, 0xEF)

# ---------------------------------------------------------------------------
# Polices et tailles
# ---------------------------------------------------------------------------

FONT_NAME = "Calibri"

FONT_SIZE_TITLE = Pt(28)
FONT_SIZE_SUBTITLE = Pt(18)
FONT_SIZE_H1 = Pt(16)
FONT_SIZE_H2 = Pt(14)
FONT_SIZE_H3 = Pt(12)
FONT_SIZE_BODY = Pt(11)
FONT_SIZE_CAPTION = Pt(9)

# ---------------------------------------------------------------------------
# Marges du document (2,5 cm sur chaque côté — identiques au doc de référence)
# ---------------------------------------------------------------------------

MARGIN_CM = Cm(2.5)

# ---------------------------------------------------------------------------
# Largeur utile d'une image dans le corps du texte (en Cm)
# ---------------------------------------------------------------------------

IMAGE_WIDTH_FULL = Cm(16)    # pleine largeur
IMAGE_WIDTH_HALF = Cm(7.5)   # demi-largeur (deux images côte à côte)

# ---------------------------------------------------------------------------
# Couleurs de fond pour les tableaux de chiffres clés
# ---------------------------------------------------------------------------

COLOR_TABLE_ROW_ODD = RGBColor(0xE8, 0xF6, 0xFD)   # bleu très pâle
COLOR_TABLE_ROW_EVEN = COLOR_WHITE
