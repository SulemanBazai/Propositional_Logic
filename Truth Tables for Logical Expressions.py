import plotly.graph_objects as go

Negation = go.Figure(data=[go.Table(
    header=dict(values=['A', '~A'],
                line_color='darkslategray',
                fill_color='plum',
                align='left'),
    cells=dict(values=[['True', 'False'],  # 1st column = A
                       ['False', 'True']],  # 2nd column = ~A
               line_color='darkslategray',
               fill_color=[['mistyrose','lavenderblush']],
               align='left'))
])

Negation.update_layout(width=500, height=300)
Negation.show()

Conjunction = go.Figure(data=[go.Table(
    header=dict(values=['A', 'B', 'A ∧ B'],
                line_color='darkslategray',
                fill_color='plum',
                align='left'),
    cells=dict(values=[['True', 'True', 'False', 'False'],  # 1st column = A
                       ['True', 'False', 'True', 'False'],  # 2nd column = B
                       ['True', 'False', 'False', 'False']],  # 3rd column = A ∧ B
               line_color='darkslategray',
               fill_color=[['mistyrose','lavenderblush','mistyrose','lavenderblush']],
               align='left'))
])

Conjunction.update_layout(width=500, height=300)
Conjunction.show()

InclusiveDisjunction = go.Figure(data=[go.Table(
    header=dict(values=['A', 'B', 'A ∨ B'],
                line_color='darkslategray',
                fill_color='plum',
                align='left'),
    cells=dict(values=[['True', 'True', 'False', 'False'],  # 1st column = A
                       ['True', 'False', 'True', 'False'],  # 2nd column = B
                       ['True', 'True', 'True', 'False']],  # 3rd column = A ∨ B
               line_color='darkslategray',
               fill_color=[['mistyrose','lavenderblush','mistyrose','lavenderblush']],
               align='left'))
])

InclusiveDisjunction.update_layout(width=500, height=300)
InclusiveDisjunction.show()

ExclusiveDisjunction = go.Figure(data=[go.Table(
    header=dict(values=['A', 'B', 'A ⊻ B'],
                line_color='darkslategray',
                fill_color='plum',
                align='left'),
    cells=dict(values=[['True', 'True', 'False', 'False'],  # 1st column = A
                       ['True', 'False', 'True', 'False'],  # 2nd column = B
                       ['False', 'True', 'True', 'False']],  # 3rd column = A ⊻ B
               line_color='darkslategray',
               fill_color=[['mistyrose','lavenderblush','mistyrose','lavenderblush']],
               align='left'))
])

ExclusiveDisjunction.update_layout(width=500, height=300)
ExclusiveDisjunction.show()

Implication = go.Figure(data=[go.Table(
    header=dict(values=['A', 'B', 'A → B'],
                line_color='darkslategray',
                fill_color='plum',
                align='left'),
    cells=dict(values=[['True', 'True', 'False', 'False'],  # 1st column = A
                       ['True', 'False', 'True', 'False'],  # 2nd column = B
                       ['True', 'False', 'True', 'True']],  # 3rd column = A → B
               line_color='darkslategray',
               fill_color=[['mistyrose','lavenderblush','mistyrose','lavenderblush']],
               align='left'))
])

Implication.update_layout(width=500, height=300)
Implication.show()

Equivalence = go.Figure(data=[go.Table(
    header=dict(values=['A', 'B', 'A ⟷ B'],
                line_color='darkslategray',
                fill_color='plum',
                align='left'),
    cells=dict(values=[['True', 'True', 'False', 'False'],  # 1st column = A
                       ['True', 'False', 'True', 'False'],  # 2nd column = B
                       ['True', 'False', 'False', 'True']],  # 3rd column = A ⟷ B
               line_color='darkslategray',
               fill_color=[['mistyrose','lavenderblush','mistyrose','lavenderblush']],
               align='left'))
])

Equivalence.update_layout(width=500, height=300)
Equivalence.show()