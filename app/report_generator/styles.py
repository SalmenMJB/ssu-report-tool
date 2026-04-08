"""
Styles et constantes visuelles pour le rapport SSU - Université d'Angers.
Les couleurs principales sont le bleu ciel et le noir, conformément à la charte
graphique de l'Université d'Angers.
"""

from docx.shared import Pt, Cm, RGBColor

# ---------------------------------------------------------------------------
# Couleurs
# ---------------------------------------------------------------------------

# Bleu ciel UA officiel (#00A8E1)
COLOR_UA_BLUE = RGBColor(0x00, 0xA8, 0xE1)

# Alias pour la rétrocompatibilité
COLOR_BLUE = COLOR_UA_BLUE
COLOR_BLUE_LIGHT = COLOR_UA_BLUE

COLOR_BLACK = RGBColor(0x00, 0x00, 0x00)
COLOR_WHITE = RGBColor(0xFF, 0xFF, 0xFF)

# Bleu ciel pâle pour alternances de tableau (#E1F5FE)
COLOR_BLUE_PALE = RGBColor(0xE1, 0xF5, 0xFE)

# Gris clair pour alternances de tableau (#F5F5F5)
COLOR_GRAY_LIGHT = RGBColor(0xF5, 0xF5, 0xF5)

# En-tête de tableaux : bleu ciel UA
COLOR_TABLE_HEADER = COLOR_UA_BLUE

# ---------------------------------------------------------------------------
# Polices et tailles
# ---------------------------------------------------------------------------

FONT_NAME = "Calibri"

FONT_SIZE_TITLE = Pt(28)
FONT_SIZE_SUBTITLE = Pt(18)
FONT_SIZE_H1 = Pt(22)
FONT_SIZE_H2 = Pt(16)
FONT_SIZE_H3 = Pt(13)
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
IMAGE_WIDTH_CHART = Cm(9)    # graphique centré standard (8-10 cm)

# ---------------------------------------------------------------------------
# Couleurs de fond pour les tableaux de chiffres clés
# ---------------------------------------------------------------------------

COLOR_TABLE_ROW_ODD = COLOR_BLUE_PALE    # bleu pâle
COLOR_TABLE_ROW_EVEN = COLOR_GRAY_LIGHT  # gris clair

# ---------------------------------------------------------------------------
# Flèches bleues pour les listes
# ---------------------------------------------------------------------------

ARROW_LEVEL1 = "➠"    # flèche niveau 1
ARROW_LEVEL2 = "➠➠"  # flèche niveau 2 (imbriquée)
