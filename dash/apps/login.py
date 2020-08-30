# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
from apps import dashboard

textbox_style={'height':'40','width':'200px','fontSize':'16','textAlign':'center'}
button_style={'height':'40','width':'208px','fontSize':'14'} 

layout = html.Div(
            children=[
                html.H1(children='Sign In Page'),
                html.Div(children=[dcc.Input(id='username', value='', type='text', placeholder='username', style=textbox_style)],style={'padding':'5px'}),
                html.Div(children=[dcc.Input(id='password', value='', type='password', placeholder='password', style=textbox_style)],style={'padding':'5px'}),
                html.Button(id='submit-button', n_clicks=0, children='Submit', style=button_style)
            ], 
            style={'textAlign':'center'}, 
            id='login_div'
        )       

@app.callback(Output('login_div', 'style'),
              [Input('submit-button', 'n_clicks')],
              [State('username', 'value'),
               State('password', 'value')])
def hide_login_div(n_clicks, user, key):
    if((user=='admin') & (key=='password')):
        return({'display':'none'})
    else:
        return({'textAlign':'center'})

@app.callback(Output('dashboard_div', 'style'),
              [Input('submit-button', 'n_clicks')],
              [State('username', 'value'),
               State('password', 'value')])
def show_dashboard_div(n_clicks, user, key):
    if((user=='admin') & (key=='password')):
        return({'textAlign':'center'})
    else:
        return({'textAlign':'center','display':'none'}) 



