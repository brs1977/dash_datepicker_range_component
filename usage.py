import datepicker_range_component
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

# suppress_callback_exceptions ID not found
app = dash.Dash(external_stylesheets=external_stylesheets,suppress_callback_exceptions=True) #assets_ignore='.*what.*'
# app = dash.Dash(suppress_callback_exceptions=True) #assets_ignore='.*what.*'

def modal(name,is_graph=False):
    return dbc.Modal(
        [
            html.Div(
                html.Section([
                    html.Div(id=name+'-title'),
                    html.Div(dbc.Button("×", id=name+'-close1', className='close'))
                ],style={'display': 'flex', 'width':'100%', 'justify-content': 'space-between'}),
            className='modal-header'),

            # dbc.ModalBody(dcc.Graph(figure=fig)),
            dcc.Graph(id=name+'-children',  config=graph_config) if is_graph else dbc.ModalBody(html.Div(id=name+'-children')) ,
            dbc.ModalFooter(
                dbc.Button("Закрыть", id=name+'-close') 
            ),

        ],
        id=name,
        size="xl",
        fade=False
        # className='fade'
    )

name_modal_table = 'modal-'

app.layout = html.Div([
    datepicker_range_component.DatepickerRange(
        id='date-picker',
        # startDate='01.05.2021',
        # endDate='19.05.2021'
        startDate='2021-05-01',
        endDate='2021-05-20'

    ),
    html.Div(id='output'),
    html.Button(id=name_modal_table+"-open", n_clicks=0, children='Submit'),
    modal('modal-'),
    
])

def toggle_modal_table(n3, n1, n2, is_open):
    return (True,[])


app.callback(
    [Output(name_modal_table, "is_open"), Output(name_modal_table+'-children','children')],
    [Input(name_modal_table+"-open", "n_clicks"), Input(name_modal_table+"-close", "n_clicks"), Input(name_modal_table+"-close1", "n_clicks")],
    [State(name_modal_table, "is_open")],
    prevent_initial_call=True
)(toggle_modal_table)


@app.callback(Output('output', 'children'), [Input('date-picker', 'startDate'),Input('date-picker', 'endDate')])
def display_output(startDate,endDate):
    return f'You have entered {startDate},{endDate}'


if __name__ == '__main__':
    app.run_server(host= '0.0.0.0',port=8035,debug=True)
