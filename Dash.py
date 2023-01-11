import dash
import dash_html_components as html
import dash_core_components as dcc
import requests
import datetime
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json

import requests
# Currency Exchange
url_currency = "https://fixer-fixer-currency-v1.p.rapidapi.com/latest"

querystring = {"base":"THB","symbols":"USD"}

headers_currency = {
	"X-RapidAPI-Key": "c7ef6b2039msh7ffcf6a6246db85p143fcfjsn6cb6b71a6935",
	"X-RapidAPI-Host": "fixer-fixer-currency-v1.p.rapidapi.com"
}

coin1 = 'BTCUSDT'
coin2 = 'BNBUSDT'
tick_interval = '1m'
key1 = "https://api.binance.com/api/v3/ticker?symbol="+coin1+"&windowSize="+tick_interval
key2 = "https://api.binance.com/api/v3/ticker?symbol="+coin2+"&windowSize="+tick_interval

app = dash.Dash(__name__, update_title=None)

app.layout = html.Div([
        html.Div([
            html.H1(
                children = "Exchange rate from 1 THB to USD",
                style = {
                    'color': '#d486f0',
                    'backgroundColor': "#18191c",
                }
            )
        ], className = 'row'),
        html.Div([ ### FIGURES Divs
            html.Div([
                dcc.Graph(id = 'fig_1' ,),
                dcc.Interval(id = 'fig_1_update' ,interval=60*1000)
            ], className = 'six columns'),
            html.Div([
                dcc.Graph(id = 'fig_2' ),
                dcc.Interval(id = 'fig_2_update', interval= 60*1000)
            ], className = 'six columns')
        ], className = 'row')])


@app.callback([Output('fig_1' , 'figure'),
               Output('fig_2' , 'figure')] , Input('fig_1_update' , 'n_intervals'))
def update_data(n):
    # Crypto Coins
    res1 = requests.get(key1)
    res2 = requests.get(key2)
    data1 = res1.json()
    data2 = res2.json()
    
    BTC_price = float(data1['openPrice'])
    BNB_price = float(data2['openPrice'])
    closeTime = data1['closeTime']
    my_datetime = datetime.datetime.fromtimestamp(closeTime / 1000)
    
    # Exchange rate
    data_currency = requests.request("GET", url_currency, headers=headers_currency, params=querystring)
    data_currency = data_currency.text
    data_currency = json.loads(data_currency)
    
    myDate = data_currency['date']
    base_currency = data_currency['base']
    rate_currency = float(data_currency['rates']['USD'])
    timeStamp = data_currency['timestamp']
    
    
    ### 
    # process the main data 
    ###

    fig_1 = make_subplots(specs=[[{"secondary_y": True}]])

    fig_1.add_trace(
    go.Scatter(x=my_datetime, y=BTC_price, name="BTC"),
    secondary_y=False,)

    fig_1.add_trace(
    go.Scatter(x=my_datetime, y=BNB_price, name="BNB"),
    secondary_y=True,)

    # Add figure title
    fig_1.update_layout(
    title_text="Compare 2 coins")

    # Set x-axis title
    fig_1.update_xaxes(title_text="Time")

    # Set y-axes titles
    fig_1.update_yaxes(title_text="BTC_Price", secondary_y=False)
    fig_1.update_yaxes(title_text="BNB_Price", secondary_y=True)

    ###
    # process data for fig 2
    ####
    fig_2 = go.Figure(
          data = go.scatter(
            x = my_datetime,
            y = rate_currency))
            
    # Add figure title
    fig_2.update_layout(
    title_text="Exchange rate from 1 THB to USD")

    # Set x-axis title
    fig_1.update_xaxes(title_text="Time")

    # Set y-axes titles
    fig_1.update_yaxes(title_text="Exchange rate", secondary_y=False)
    
    return [ fig_1 , fig_2]


if __name__ == '__main__':
    app.run_server()


