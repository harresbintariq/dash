import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from datetime import datetime as dt
from app import app
import flask
import io

class_dropdown_values=['1','2','3']
button_style={'display':'inline-block','verticalAlign':'middle', 'width':'45%','height':'38px','backgroundColor':'rgb(158,202,225)','font-weight':'bold'}
drop_style={'display':'inline-block','verticalAlign':'middle', 'padding':'1.5%','width':'50%'}

layout = html.Div(
                    children=[
                        html.H2(id='control_heading', children='Control Panel', style={'textAlign':'center'}),
                        html.H3(id='Enable_heading', children='Application Toggle'),
                        dcc.Checklist(
                            options=[
                                {'label': 'Enabled', 'value': 'E'},
                            ],
                            values=['E']
                        ),
                        html.H3(id='Frequency_heading', children='Frequency Calibration'),
                        html.Label('Frequency of Classification'),
                        html.Div(
                            children=[
                                html.Button(id='classify-button', n_clicks=0, children='Classify',style=button_style),
                                html.Div(
                                    dcc.Dropdown(
                                            id='class_dropdown',
                                            options=[{'label': i, 'value': i} for i in class_dropdown_values],
                                            value='3'
                                    ),
                                    style=drop_style
                                )
                            ]
                        ),
                        html.Label('Frequency of Training'),
                        html.Div(
                            children=[
                                html.Button(id='train-button', n_clicks=0, children='Train',style=button_style),
                                html.Div(
                                    dcc.Dropdown(
                                            id='train_dropdown',
                                            options=[{'label': i, 'value': i} for i in class_dropdown_values],
                                            value='2'
                                    ),
                                    style=drop_style
                                )
                            ]
                        ),
                        html.H3(id='Reports',children='Data Statistics'),
                        dcc.DatePickerRange(
                            id='my-date-picker-range',
                            min_date_allowed=dt(2019, 1, 1),
                            max_date_allowed=dt.now(),
                            initial_visible_month=dt(2019, 1, 1),
                            with_portal=True,
                            #clearable=True
                            #calendar_orientation='vertical'
                            #start_date=dt(2017, 8, 25)
                        ),
                        html.Label(''),
                        html.Button(id='report-button', n_clicks=0, children='Create Report',style={'width':'85%','height':'38px','backgroundColor':'rgb(158,202,225)','font-weight':'bold'}),
                        html.A(
                            children='ReportLink',
                            href='',
                            id='my-link',
                            #target='_blank',
                            style={'position':'absolute','bottom':'20%','left':'1.5%','display':'none'}
                        )
                    ],
                    id='control_div',
                    style={'padding':'0.25%','display':'inline-block','maxWidth':'22%','height':'100%','boxShadow':'5px 5px 5px grey','position':'absolute','left':'0','top':'38px'}#'float':'left'}#,'zIndex':'4','backgroundColor':'#EEEEEE'}#,'marginLeft':'0px','borderLeft':'1px solid black'}#400,'verticalAlign':'middle','borderRight':'4px dotted #1f77b4','float':'left',
        )


@app.callback(Output('my-link', 'style'), [Input('report-button', 'n_clicks')])
def report_link_visible(value):
    print(value)
    if(value>0):
        style = {'position':'absolute','bottom':'20%','left':'1.5%'}
    else:
        style = {'position':'absolute','bottom':'20%','left':'1.5%','display':'none'}

    return(style)


@app.callback(Output('my-link', 'children'), [Input('report-button', 'n_clicks')], [State('my-date-picker-range','start_date'), State('my-date-picker-range','end_date')])
def update_report_link(value, start_date, end_date):
    string_prefix = 'Report link: '
    if start_date is not None:
        start_date = dt.strptime(start_date, '%Y-%m-%d')
        start_date_string = start_date.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
    if end_date is not None:
        end_date = dt.strptime(end_date, '%Y-%m-%d')
        end_date_string = end_date.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'End Date: ' + end_date_string
    if len(string_prefix) == len('You have selected: '):
        return 'Select a date to see it displayed here'
    else:
        return string_prefix

@app.callback(Output('my-link', 'href'), [Input('report-button', 'n_clicks')])
def download_report(value):
    return '/dash/urlToDownload'

@app.server.route('/dash/urlToDownload')
def download_file():
    return flask.send_file('./apps/abc.xlsx', as_attachment=True)