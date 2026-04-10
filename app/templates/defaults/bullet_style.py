"""
Style des bullets avec flèches bleu ciel.
"""

from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

BULLET_ICON = "➡️"
BULLET_COLOR = RGBColor(0, 153, 204)  # Bleu ciel
BULLET_FONT_SIZE = Pt(11)
BULLET_INDENT_LEVEL_0 = 0.5  # cm
BULLET_INDENT_LEVEL_1 = 1.0  # cm
BULLET_INDENT_LEVEL_2 = 1.5  # cm

def get_bullet_indent(level: int) -> float:
    """Retourne l'indentation selon le niveau"""
    indents = {
        0: BULLET_INDENT_LEVEL_0,
        1: BULLET_INDENT_LEVEL_1,
        2: BULLET_INDENT_LEVEL_2,
    }
    return indents.get(level, BULLET_INDENT_LEVEL_0)