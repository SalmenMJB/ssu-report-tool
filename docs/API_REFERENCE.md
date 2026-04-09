# Référence API - ReportBuilder

## ReportBuilder

Classe principale pour construire le document.

### `__init__(output_path: str)`
Initialise le builder.

```python
builder = ReportBuilder("output/rapport.docx")

Titres
add_chapter_title(title: str)
Ajoute un titre de chapitre (H1).
builder.add_chapter_title("Service infirmier")

add_section_title(title: str, number: int = None)
Ajoute un titre de section (H2).
builder.add_section_title("Faits marquants de l'année", number=1)

Listes
add_bullet_point(text: str, level: int = 0)
Ajoute une bullet avec flèche.
builder.add_bullet_point("4 infirmières à Angers")
builder.add_bullet_point("Détail du point", level=1)

Encadrés
add_highlighted_box(text: str, color: str = 'cyan')
Ajoute un encadré avec bordure bleu ciel.
builder.add_highlighted_box("Texte important")

Tableaux
add_key_indicators_table(indicators: dict, title: str = None)
Ajoute un tableau de chiffres clés.
builder.add_key_indicators_table({
    "Nombre de sessions": 22,
    "Participants": 325,
}, title="Chiffres clés – PSSM")

Graphiques
add_pie_chart(data: list, labels: list, caption: str = "")
Ajoute un pie chart.
builder.add_pie_chart(
    [46, 21, 8, 2, 6],
    ['UCO', 'ESA', 'ARIFTS', 'Campus de Pouillé', 'ENSAM'],
    caption="Répartition des effectifs"
)

add_bar_chart(data: list, categories: list, caption: str = "")
Ajoute un bar chart.
builder.add_bar_chart(
    [1596, 359, 7868, 1206],
    ['Bilans santé', 'Internationaux', 'Consultations', 'Certificats'],
    caption="Évolution des consultations"
)

add_line_chart(data: list, labels: list, x_axis: list, caption: str = "")
Ajoute une courbe.
builder.add_line_chart(
    [[247, 260, 352, 340, 465, 517, 529, 684, 753, 810, 995]],
    ['2024-2025'],
    ['2014-15', '2015-16', '2016-17', ...],
    caption="Évolution aménagements"
)

Document
save()
Sauvegarde le document.
builder.save()


Composants
components.titles
from app.report_generator.components.titles import add_chapter_title
add_chapter_title(builder, "Titre du chapitre")

components.bullets
from app.report_generator.components.bullets import add_bullet
add_bullet(builder, "Texte de la bullet", level=0)

components.boxes
from app.report_generator.components.boxes import add_highlighted_box
