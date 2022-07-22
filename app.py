######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash import Input, Output, State
import os

###### Set up variables
list_of_choices=[' ', 'Squat', 'Chest Press', 'Pull Up']
githublink = 'https://github.com/cryswong26/201-chuck-norris-callback'
#image1='Orion Gym.jpg'
list_of_pics=['Orion Gym.jpg', 'Squat.gif', 'Chest Press.gif', 'Pull Up.gif']
heading1='My Favorite Exercises'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Exercises'

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    html.Br(),
    #html.Img(src=app.get_asset_url(image1), style={'width': 'auto', 'height': '10%'}),
    #dcc.Dropdown(id='your-input-here',
                #options=[{'label': i, 'value': i} for i in list_of_choices],
                #value='squat',
                #style={'width': '500px'}),
    dcc.Dropdown(id='your-input-here',
                options=[
                    {'label':list_of_choices[0], 'value':list_of_pics[0]},
                    {'label':list_of_choices[1], 'value':list_of_pics[1]},
                    {'label':list_of_choices[2], 'value':list_of_pics[2]},
                    {'label':list_of_choices[3], 'value':list_of_pics[3]},
                ],
                value=list_of_pics[0], #the starting value
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.Div(id='output-message', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback(
    [Output('your-output-here', 'children'),
    Output('output-message', 'children')],
    [Input('your-input-here', 'value')],
             )
def multi_output(whatever_you_chose):
    if whatever_you_chose is None:
        raise PreventUpdate
    image = html.Img(src=app.get_asset_url(whatever_you_chose), style={'width': 'auto', 'height': '50%'})
    split_list = whatever_you_chose.split('.',1)
    message = 'Here is a '+split_list[0]+'!'
    #message = f'Here is a {whatever_you_chose}!'
    return image, message

#def display_value(whatever_you_chose):
#    return f'I will now show you a {whatever_you_chose}.'


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
