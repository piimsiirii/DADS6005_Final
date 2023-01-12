import dash
from dash import html
from dash import dcc
import requests
import datetime
from dash.dependencies import Input, Output
import json
from river import metrics
import joblib

# Currency Exchange
url_currency = "https://fixer-fixer-currency-v1.p.rapidapi.com/latest"

querystring = {"base":"USD","symbols":"THB"}

headers_currency = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "fixer-fixer-currency-v1.p.rapidapi.com"
}

# Gold Price
url_gold = "https://gold-price1.p.rapidapi.com/get_price/USD"

headers_gold = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "gold-price1.p.rapidapi.com"
}

# Model River
metric = metrics.MSE()
model = joblib.load('GoldPrice.sav')

output_data = dict(x=[], y1=[], y2=[])


figure = dict(
    data=[
        {'x': output_data['x'], 'y': output_data['y1'], 'type': 'line', 'name': 'Exchange_rate (THB/USD)'},
        {'x': output_data['x'], 'y': output_data['y2'], 'type': 'line', 'name': 'Gold_Price (USD)', 'yaxis': 'y2'}
    ], 
    layout=dict(
        xaxis=dict(title='DateTime'), 
        yaxis=dict(title='Exchange_rate (THB/USD)'),
        yaxis2=dict(title='Gold_Price (USD)', overlaying='y', side='right')
    )
)

app = dash.Dash(__name__, update_title=None)

app.layout = html.Div(
        [   
            html.H1(children='EXCHANGE RATE(THB/USD) VS. GOLD PRICE(USD)', style = {'color': '#000000', 'backgroundColor': "#E2B741"}),
            dcc.Graph(id='graph', figure=figure), 
            dcc.Interval(id="interval",interval= 60*1000),
            html.H1(children='Model Predict Gold Price', style = {'color': '#000000', 'backgroundColor': "#E2B741"}),
            html.Div(id='text1', style={'font-size':25}),
            html.Div(id='text2', style={'font-size':25}),
            html.Div(id='text3', style={'font-size':25})
		]
	)
    
@app.callback(
    Output('graph', 'figure'), 
    [Input('interval', 'n_intervals')])
	
def update_graph(n_intervals):
    data_currency = requests.request("GET", url_currency, headers=headers_currency, params=querystring)
    data_currency = data_currency.text
    data_currency = json.loads(data_currency)
    
    data_gold = requests.request("GET", url_gold, headers=headers_gold)
    data_gold = data_gold.text
    data_gold = json.loads(data_gold)
    
    rate_currency = float(data_currency['rates']['THB'])
    goldPrice = float(data_gold['gold']['price'])
    timeStamp = data_currency['timestamp']
    my_datetime = datetime.datetime.fromtimestamp(timeStamp)
    

    output_data['x'].append(my_datetime)
    output_data['y1'].append(rate_currency)
    output_data['y2'].append(goldPrice)

    figure = dict(
        data=[
            {'x': output_data['x'], 'y': output_data['y1'], 'type': 'line', 'name': 'Exchange_rate (THB/USD)'},
            {'x': output_data['x'], 'y': output_data['y2'], 'type': 'line', 'name': 'Gold_Price (USD)', 'yaxis': 'y2'}
        ], 
        layout=dict(
            xaxis=dict(title='DateTime'), 
            yaxis=dict(title='Exchange_rate (THB/USD)'),
            yaxis2=dict(title='Gold_Price (USD)', overlaying='y', side='right')
        )
    )

    return figure
 
#---------------------------------------------------------- 
@app.callback(
    [Output('text1', 'children'), Output('text2', 'children'), Output('text3', 'children')], 
    [Input('interval', 'n_intervals')])
    
def update_graph(n_intervals):
    data_currency = requests.request("GET", url_currency, headers=headers_currency, params=querystring)
    data_currency = data_currency.text
    data_currency = json.loads(data_currency)
    rate_currency = data_currency['rates']
    
    data_gold = requests.request("GET", url_gold, headers=headers_gold)
    data_gold = data_gold.text
    data_gold = json.loads(data_gold)
    goldPrice = data_gold['gold']['price']
    
    price_pred = model.predict_one(rate_currency)
    model.learn_one(rate_currency, goldPrice)
    metric.update(goldPrice, price_pred)
    
    realPrice = f"Real price: {goldPrice}"
    predictPrice = f"Predict price: {price_pred}"
    mse_score = f"{metric}"
    
    return (realPrice, predictPrice, mse_score)
    
if __name__ == '__main__':
    app.run_server()
