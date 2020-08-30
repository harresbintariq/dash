import io

import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(id='my-dropdown', value='default',
                 options=[
                     {'label': 'New York City', 'value': 'NYC'},
                     {'label': 'Montréal', 'value': 'MTL'},
                     {'label': 'San Francisco', 'value': 'SF'}
                 ]
                 ),
    #html.A('Download CSV', id='my-link'),
    #html.Button(id='report-button', n_clicks=0, children='Download Report',style={'width':'318px','backgroundColor':'rgb(158,202,225)'})
    html.A(html.Button(id='report-button', n_clicks=0, children='Download Report',style={'width':'318px','backgroundColor':'rgb(158,202,225)'}),
    href='',
    id='my-link')
])


# @app.callback(Output('my-link', 'href'), [Input('my-dropdown', 'value')])
# def update_link(value):
#     return '/dash/urlToDownload?value={}'.format(value)

@app.callback(Output('my-link', 'href'), [Input('report-button', 'n_clicks')])
def download_report(value):
    return '/dash/urlToDownload?value={}'.format(value)


@app.server.route('/dash/urlToDownload')
def download_csv():
    value = flask.request.args.get('value')
    # create a dynamic csv or file here using `StringIO`
    # (instead of writing to the file system)
    str_io = io.StringIO()
    str_io.write('You have selected {}'.format(value))
    mem = io.BytesIO()
    mem.write(str_io.getvalue().encode('utf-8'))
    mem.seek(0)
    str_io.close()
    return flask.send_file(mem,
                           mimetype='text/csv',
                           attachment_filename='downloadFile.csv',
                           as_attachment=True)


if __name__ == '__main__':
    app.run_server(debug=True)