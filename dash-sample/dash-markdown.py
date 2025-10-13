"""layout markdown."""

from dash import Dash, dcc, html


app = Dash()

markdown_text = """
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
"""

app.layout = html.Div([dcc.Markdown(children=markdown_text)])

if __name__ == "__main__":
    app.run(debug=True)
