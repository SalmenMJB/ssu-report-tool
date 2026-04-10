"""
Styles des tableaux (en-têtes, lignes alternées, bordures).
"""

from docx.shared import RGBColor, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Couleurs
HEADER_BACKGROUND = RGBColor(0, 153, 204)  # Bleu ciel
HEADER_TEXT_COLOR = RGBColor(255, 255, 255)  # Blanc
ROW_ALTERNATE_COLOR = RGBColor(245, 245, 245)  # Gris clair
BORDER_COLOR = RGBColor(204, 204, 204)  # Gris

# Texte
HEADER_FONT_SIZE = Pt(11)
HEADER_FONT_BOLD = True
CELL_FONT_SIZE = Pt(11)
CELL_PADDING = 6  # pt

# Alignement
HEADER_ALIGNMENT = WD_ALIGN_PARAGRAPH.CENTER
CELL_ALIGNMENT = WD_ALIGN_PARAGRAPH.LEFT

# Configuration complète
TABLE_CONFIG = {
    'header': {
        'background': HEADER_BACKGROUND,
        'text_color': HEADER_TEXT_COLOR,
        'font_size': HEADER_FONT_SIZE,
        'bold': HEADER_FONT_BOLD,
        'alignment': HEADER_ALIGNMENT,
    },
    'cells': {
        'font_size': CELL_FONT_SIZE,
        'padding': CELL_PADDING,
        'alignment': CELL_ALIGNMENT,
    },
    'alternating': {
        'even_color': RGBColor(255, 255, 255),  # Blanc
        'odd_color': ROW_ALTERNATE_COLOR,  # Gris clair
    },
    'border': {
        'color': BORDER_COLOR,
        'width': 1,  # pt
    }
}