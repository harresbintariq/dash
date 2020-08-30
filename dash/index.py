import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import sys
sys.path.append('D:\dash')
from app import app
from apps import login, dashboard

app.layout=html.Div(
                children=[
                    #login.layout,
                    dashboard.layout
                ]
            )


if __name__ == '__main__':
    app.run_server(debug=True)