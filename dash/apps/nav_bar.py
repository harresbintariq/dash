import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from app import app
import base64

#image_filename='/Users/harresbintariq/Documents/thefolder/dash/joker.png'
#encoded_image = base64.b64encode(open(image_filename, 'rb').read())

button_style_logout={'width':'10%', 'height':'5.3%','backgroundColor':'rgb(158,202,225)','display':'inline-block','verticalAlign':'middle','position':'absolute','right':'0','top':'0','font-weight':'bold'}
button_style_settings={'width':'10%','height':'5.3%','backgroundColor':'rgb(158,202,225)','display':'inline-block','verticalAlign':'middle','position':'absolute','right':'11%','top':'0','font-weight':'bold'}


layout = html.Div(
                    children=[
                        html.H3(id='dashboard_heading',children='',style={'textAlign':'center','display':'inline-block','verticalAlign':'middle'}),
                        #html.Img(id='image',src='data:image/png;base64,{}'.format(encoded_image)),
                        #html.Img(id='image',src=image_filename,alt='Logo',style={'width':'200px','color':'white'}),
                        html.Button(id='logout-button', n_clicks=0, children='Logout',style=button_style_logout),
                        html.Button(id='settings-button', n_clicks=0, children='Settings',style=button_style_settings)
                    ],
                    id='nav_div',
                    style={'boxShadow':'0px 0px 20px black','float':'top','border':'0','height':'38px'}#,'zIndex':'9'}#,'marginLeft':'0px','borderLeft':'1px solid black'}#400,'verticalAlign':'middle','borderRight':'4px dotted #1f77b4','float':'left','backgroundColor':'#EEEEEE',
        )