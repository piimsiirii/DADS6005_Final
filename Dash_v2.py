import dash
import dash_html_components as html
import dash_core_components as dcc
import requests
import datetime
from dash.dependencies import Input, Output
import json

# Currency Exchange
url_currency = "https://fixer-fixer-currency-v1.p.rapidapi.com/latest"

querystring = {"base":"THB","symbols":"USD"}

headers_currency = {
	"X-RapidAPI-Key": "c7ef6b2039msh7ffcf6a6246db85p143fcfjsn6cb6b71a6935",
	"X-RapidAPI-Host": "fixer-fixer-currency-v1.p.rapidapi.com"
}


figure = dict(
    data=[{'x': [], 'y': []}], 
    layout=dict(
        xaxis=dict(range=[]), 
        yaxis=dict(range=[])
        )
    )

app = dash.Dash(__name__, update_title=None)  # remove "Updating..." from title

app.layout = html.Div(
        [
            dcc.Graph(id='graph', figure=figure), 
            dcc.Interval(id="interval",interval=1*60*1000)
        ]
    )

@app.callback(
    Output('graph', 'extendData'), 
    [Input('interval', 'n_intervals')])
    
def update_data(n_intervals):

    print("interval ",n_intervals)

    data_currency = requests.request("GET", url_currency, headers=headers_currency, params=querystring)
    data_currency = data_currency.text
    data_currency = json.loads(data_currency)
    print(data_currency)
    
    myDate = data_currency['date']
    base_currency = data_currency['base']
    rate_currency = float(data_currency['rates']['USD'])
    timeStamp = data_currency['timestamp']
    my_datetime = datetime.datetime.fromtimestamp(timeStamp)   

    return dict(x=[[my_datetime]], y=[[rate_currency]])
    
if __name__ == '__main__':
    app.run_server()