import plotly.graph_objects as go

DoubleNegation = go.Figure(data=[go.Table(
    header=dict(values=['A', '~A', '~~A'],
                line_color='darkslategray',
                fill_color='plum',
                align='left'),
    cells=dict(values=[['True', 'False'],  # 1st column = A
                       ['False', 'True'],  # 2nd column = ~A
                       ['True', 'False']],  # 3rd column = ~~A
               line_color='darkslategray',
               fill_color=[['mistyrose','lavenderblush','mistyrose','lavenderblush']],
               align='left'))
])

DoubleNegation.update_layout(width=500, height=300)
DoubleNegation.show()

CommutativityOfConjunction = go.Figure(data=[go.Table(
    header=dict(values=['A', 'B', 'A ∧ B', 'B ∧ A'],
                line_color='darkslategray',
                fill_color='plum',
                align='left'),
    cells=dict(values=[['True', 'True', 'False', 'False'],  # 1st column = A
                       ['True', 'False', 'True', 'False'],  # 2nd column = B
                       ['True', 'False', 'False', 'False'],  # 3rd column = A ∧ B
                       ['True', 'False', 'False', 'False']],  # 4th column = B ∧ A
               line_color='darkslategray',
               fill_color=[['mistyrose','lavenderblush','mistyrose','lavenderblush']],
               align='left'))
])

CommutativityOfConjunction.update_layout(width=500, height=300)
CommutativityOfConjunction.show()

CommutativityOfDisjunction = go.Figure(data=[go.Table(
    header=dict(values=['A', 'B', 'A ∨ B', 'B ∨ A'],
                line_color='darkslategray',
                fill_color='plum',
                align='left'),
    cells=dict(values=[['True', 'True', 'False', 'False'],  # 1st column = A
                       ['True', 'False', 'True', 'False'],  # 2nd column = B
                       ['True', 'True', 'True', 'False'],  # 3rd column = A ∨ B
                       ['True', 'True', 'True', 'False']],  # 4th column = B ∨ A
               line_color='darkslategray',
               fill_color=[['mistyrose','lavenderblush','mistyrose','lavenderblush']],
               align='left'))
])

CommutativityOfDisjunction.update_layout(width=500, height=300)
CommutativityOfDisjunction.show()

AssociativityOfConjunction = go.Figure(data=[go.Table(
    header=dict(values=['A', 'B', 'C', 'A ∧ B', 'B ∧ C', 'A ∧ (B ∧ C)', '(A ∧ B) ∧ C'],
                line_color='darkslategray',
                fill_color='plum',
                align='left'),
    cells=dict(values=[['True', 'True', 'True', 'True', 'False', 'False', 'False', 'False'],  # 1st column = A
                       ['True', 'True', 'False', 'False', 'True', 'True', 'False', 'False'],  # 2nd column = B
                       ['True', 'False', 'True', 'False', 'True', 'False', 'True', 'False'],  # 3rd column = C
                       ['True', 'True', 'False', 'False', 'False', 'False', 'False', 'False'],  # 4th column = A ∧ B
                       ['True', 'False', 'False', 'False', 'True', 'False', 'False', 'False'],  # 5th column = B ∧ C
                       ['True', 'False', 'False', 'False', 'False', 'False', 'False', 'False'],  # 6th column = A ∧ (B ∧ C)
                       ['True', 'False', 'False', 'False', 'False', 'False', 'False', 'False']],  # 7th column = (A ∧ B) ∧ C
               line_color='darkslategray',
               fill_color=[['mistyrose','lavenderblush','mistyrose','lavenderblush']],
               align='left'))
])

AssociativityOfConjunction.update_layout(width=500, height=300)
AssociativityOfConjunction.show()

AssociativityOfDisjunction = go.Figure(data=[go.Table(
    header=dict(values=['A', 'B', 'C', 'A ∨ B', 'B ∨ C', 'A ∨ (B ∨ C)', '(A ∨ B) ∨ C'],
                line_color='darkslategray',
                fill_color='plum',
                align='left'),
    cells=dict(values=[['True', 'True', 'True', 'True', 'False', 'False', 'False', 'False'],  # 1st column = A
                       ['True', 'True', 'False', 'False', 'True', 'True', 'False', 'False'],  # 2nd column = B
                       ['True', 'False', 'True', 'False', 'True', 'False', 'True', 'False'],  # 3rd column = C
                       ['True', 'True', 'True', 'True', 'True', 'True', 'False', 'False'],  # 4th column = A ∨ B
                       ['True', 'True', 'True', 'False', 'True', 'True', 'True', 'False'],  # 5th column = B ∨ C
                       ['True', 'True', 'True', 'True', 'True', 'True', 'True', 'False'],  # 6th column = A ∨ (B ∨ C)
                       ['True', 'True', 'True', 'True', 'True', 'True', 'True', 'False']],  # 7th column = (A ∨ B) ∨ C
               line_color='darkslategray',
               fill_color=[['mistyrose','lavenderblush','mistyrose','lavenderblush']],
               align='left'))
])

AssociativityOfDisjunction.update_layout(width=500, height=300)
AssociativityOfDisjunction.show()

DeMorganConjunction = go.Figure(data=[go.Table(
    header=dict(values=['A', 'B', '~A', '~B', 'A ∧ B', '~(A ∧ B)', '~A ∨ ~B'],
                line_color='darkslategray',
                fill_color='plum',
                align='left'),
    cells=dict(values=[['True', 'True', 'False', 'False'],  # 1st column = A
                       ['True', 'False', 'True', 'False'],  # 2nd column = B
                       ['False', 'False', 'True', 'True'],  # 3rd column = ~A
                       ['False', 'True', 'False', 'True'],  # 4th column = ~B
                       ['True', 'False', 'False', 'False'],  # 5th column = A ∧ B
                       ['False', 'True', 'True', 'True'],  # 6th column = ~(A ∧ B)
                       ['False', 'True', 'True', 'True']],  # 7th column = ~A ∨ ~B
               line_color='darkslategray',
               fill_color=[['mistyrose','lavenderblush','mistyrose','lavenderblush']],
               align='left'))
])

DeMorganConjunction.update_layout(width=500, height=300)
DeMorganConjunction.show()

DeMorganDisjunction = go.Figure(data=[go.Table(
    header=dict(values=['A', 'B', '~A', '~B', 'A ∨ B', '~(A ∨ B)', '~A ∧ ~B'],
                line_color='darkslategray',
                fill_color='plum',
                align='left'),
    cells=dict(values=[['True', 'True', 'False', 'False'],  # 1st column = A
                       ['True', 'False', 'True', 'False'],  # 2nd column = B
                       ['False', 'False', 'True', 'True'],  # 3rd column = ~A
                       ['False', 'True', 'False', 'True'],  # 4th column = ~B
                       ['True', 'True', 'True', 'False'],  # 5th column = A ∨ B
                       ['False', 'False', 'False', 'True'],  # 6th column = ~(A ∨ B)
                       ['False', 'False', 'False', 'True']],  # 7th column = ~A ∧ ~B
               line_color='darkslategray',
               fill_color=[['mistyrose','lavenderblush','mistyrose','lavenderblush']],
               align='left'))
])

DeMorganDisjunction.update_layout(width=500, height=300)
DeMorganDisjunction.show()

# Still need to add Distributive Laws.
