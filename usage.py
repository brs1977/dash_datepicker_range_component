import datepicker_range_component
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    datepicker_range_component.DatepickerRange(
        id='date-picker',
        # startDate='01.05.2021',
        # endDate='19.05.2021'
        startDate='2021-05-01',
        endDate='2021-05-20'

    ),
    html.Div(id='output')
])


@app.callback(Output('output', 'children'), [Input('date-picker', 'startDate'),Input('date-picker', 'endDate')])
def display_output(startDate,endDate):
    return f'You have entered {startDate},{endDate}'


if __name__ == '__main__':
    app.run_server(port=8035,debug=True)
