import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
from apps import control_panel as cp
from apps import bar_graph as bg
from apps import doughnut as dg
from apps import nav_bar as nb

layout = html.Div(
            children=[
                nb.layout,
                cp.layout,
                bg.layout,
                dg.layout
            ], 
            id='dashboard_div',
            style={'width':'100%','overflow':'hidden','position':'absolute','top':'0','right':'0','bottom':'0','left':'0'},
        )

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

    
