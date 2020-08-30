import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from app import app
#from apps import graph_stats as gs
import numpy as np
import json
import flask


def populate_graph():
#    statsorted=gs.get_stats()
#    x=[statsorted[i]['label'] for i in range(0,len(statsorted))]
#    total=[int(statsorted[i]['count']) for i in range(0,len(statsorted))]
#    correct=[int(statsorted[i]['sn']) for i in range(0,len(statsorted))]
#    incorrect=list(np.array(total)-np.array(correct))
#    
    x=['2019-02-03','2019-02-04','2019-02-05','2019-02-06','2019-02-07','2019-02-08']
    correct=[249,345,653,67,243,565]
    incorrect=[45,89,120,10,50,76]
    xaxis={
        'tickformat':'%Y-%m-%d',
        'tickangle':-45,
        'dtick':86400000.0
        }
    yaxis={
        'title':'No. of Events'
    }

    graph_layout=go.Layout(
        {
            'title':'Historical Trend',
            'barmode':'stack',
            'xaxis':xaxis,
            'yaxis':yaxis,
            'autosize':False,
            'width':650,
            'height':520,
            'legend':{'x':0.7,'y':1.05,'orientation':'h'}
        }
    )
    
    trace1=go.Bar(x=x,y=correct,name='Correct')
    trace2=go.Bar(x=x,y=incorrect,name='Incorrect',marker={'color':'rgb(158,202,225)'})

    data=[trace1,trace2]

    fig={
            'data':data,
            'layout':graph_layout
        }

    return(fig)

fig=populate_graph()

layout=html.Div(
            children=[
                #html.A(
                dcc.Graph(
                    id='graph',
                    figure=fig
                ),#id='report_link',href=''),
#                dcc.Interval(
#                    id='interval_component',
#                    interval=app.update_interval*1000, # in milliseconds
#                    n_intervals=0
#                )
            ],
            id='graph_div',
            style={'maxWidth':'600px','display':'inline-block','padding':'1.1%','height':'100vh','position':'absolute','left':'26%','top':'7.5%'}#,'verticalAlign':'middle'},  #650  
        )


@app.callback(Output('graph','figure'),
            [Input('interval_component','n_intervals')]
)
def update_graph(n):
    fig=populate_graph()
    print('update')
    return(fig)

# @app.callback(Output('my-link', 'href'), [Input('graph', 'clickData')])
# def download_graph_report(value):
#     return '/dash/urlToDownload?value={}'.format(value)

# @app.callback(Output('graph_div', 'style'), [Input('graph', 'clickData')])
# #@app.callback(Output('report_link', 'href'), [Input('graph', 'clickData')])
# def download_graph_report(value):
#     print(value)
#     #return '/dash/graph/urlToDownload?value={}'.format(value)
#     return({'maxWidth':'600px','display':'inline-block'})

# @app.server.route('/dash/graph/urlToDownload')
# def download_graph_file():
#     return flask.send_file('./apps/dashboard.py', as_attachment=True)

