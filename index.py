import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from app import app
from apps import home, industry_mapping, product_mapping

server = app.server



# App Layout
app.layout = html.Div(children=[
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ]
)



# Callbacks
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/':
        return home.layout
    if pathname == '/home':
        return home.layout
    elif pathname == '/apps/industry_mapping':
        return industry_mapping.layout
    elif pathname == '/apps/product_mapping':
        return product_mapping.layout
    else:
        return '404'



if __name__ == '__main__':
    app.run_server(debug=False)
