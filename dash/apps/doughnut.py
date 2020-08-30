import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import numpy as np
#from apps import graph_stats as gs
from app import app

def populate_pie():
#    statsorted=gs.get_stats()
#    total=[int(statsorted[i]['count']) for i in range(0,len(statsorted))]
#    correct=[int(statsorted[i]['sn']) for i in range(0,len(statsorted))]
#    incorrect=list(np.array(total)-np.array(correct))
#    x=['1','2','3','4','5','6']
    correct=[249,345,653,67,243,565]
    incorrect=[45,89,120,10,50,76]
    values=[np.sum(correct),np.sum(incorrect)]
    labels=['Correct','Incorrect']
    colors=['#1f77b4','rgb(158,202,225)']
    
    fig = {
  "data": [
    {
      "values": values,
      "labels": labels,
      "domain": {"x": [0.0, 1]},
      "name": "Summary",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie",
      "marker":{"colors":colors}
    }
    ],
  "layout": {
        "title":"Summary",
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "",
                "x": 0.20,
                "y": 0.5
            }
        ],
        'height':520,
        #'legend':{'x':'0.7','y':'1.05','orientation':'h'}
    }
}
    return(fig)

fig=populate_pie()

layout=html.Div(
            children=[
                dcc.Graph(
                    id='pie_graph',
                    figure=fig
                ),
#                dcc.Interval(
#                    id='pie_interval_component',
#                    interval=app.update_interval*1000, # in milliseconds
#                    n_intervals=0
#                )
            ],
            id='pie_div',
            style={'maxWidth':'28%','display':'inline-block','padding':'1.1%','position':'absolute','right':'0','top':'7.5%'}  #650 ,'verticalAlign':'middle' ,'float':'right'
        )

@app.callback(Output('pie_graph','figure'),
            [Input('pie_interval_component','n_intervals')]
)
def update_pie(n):
    fig=populate_pie()
    return(fig)