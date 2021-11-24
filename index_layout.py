import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("github", href="https://github.com/jtn243/Expalinable-AI"),
            ],
            nav=True,
            in_navbar=True,
            label="Source",
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("readthedocs", href="http://explainerdashboard.readthedocs.io/en/latest/"),
                dbc.DropdownMenuItem("pypi", href="https://pypi.org/project/explainerdashboard/"),
            ],
            nav=True,
            in_navbar=True,
            label="explainerdashboard",
        ),
        
    ],
    brand="Cryptocurrency Expalinable-AI",
    brand_href="https://github.com/jtn243/Expalinable-AI",
    color="primary",
    dark=True,
    fluid=True,
)

trend_card = dbc.Card(
    [
        dbc.CardImg(src="assets/trend.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Classifier Dashboard", className="card-title"),
                html.P(
                    "Predicting the Trend of Bitcoin for last 30 Days"
                    ,className="card-text",
                ),
                html.A(dbc.Button("Go to dashboard", color="primary"),
                       href="/classifier"),
                dbc.Button("Show Code", id="clas-code-modal-open", className="mr-1"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Code needed for this Classifier Dashboard"),
                        dcc.Markdown(
"""
```python
import pandas as pd
from pathlib import Path
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestRegressor
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard


pkl_dir = Path.cwd() / "pkls"
data_dir= Path.cwd() / "data"

btc = pd.read_csv(data_dir /'BTC_pro.csv', index_col=0)

feature_descriptions={
        'Open': 'Opening Price',
        'Close': 'Closing Price',
        'Low': 'Lowest Price',
        'High': 'Highest Price',
        'Volume': 'A measure of how much of a cryptocurrency was traded in the last 24 hours',
        'Market Cap': "The total market value of a cryptocurrency's circulating supply",
        'Return' : 'Return on the Single Day',
        'Cum_Return':'Cummulative Return',
        'Trend': 'Up or Down'}

X = btc.drop(columns=['Trend','Return'], axis=1)
y = btc['Trend']

X_train = X.iloc[0:len(X)-30, :]
X_test= X.iloc[len(X)-30: , :]
y_train = y.iloc[0:len(X)-30]
y_test = y.iloc[len(X)-30:]

oversample = SMOTE()
X_train,y_train = oversample.fit_resample(X_train,y_train)

rfc = RandomForestClassifier()
rfc.fit(X_train,y_train)
rfc_pred = rfc.predict(X_test)

explainer_c = ClassifierExplainer(rfc, X_test, y_test, X_background=X_train,descriptions=feature_descriptions , 
                                  target='Trend', labels=['Down','Up'])
_ = ExplainerDashboard(explainer_c)
explainer_c.dump(pkl_dir /"explainer_c.joblib")
```
"""
                        ),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="clas-code-modal-close", className="ml-auto")
                        ),
                    ],
                    id="clas-code-modal",
                    size="lg",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)

price_card = dbc.Card(
    [
        dbc.CardImg(src="assets/price.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Regression Dashboard", className="card-title"),
                html.P(
                    "Predicting the Close Price of Bitcoin for last 30 Days"
                    ,className="card-text",
                ),
                html.A(dbc.Button("Go to dashboard", color="primary"),
                       href="/regression"),
                dbc.Button("Show Code", id="reg-code-modal-open", className="mr-1"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Code needed for this Regression Dashboard"),
                        dcc.Markdown(
"""
```python
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard


pkl_dir = Path.cwd() / "pkls"
data_dir= Path.cwd() / "data"

btc = pd.read_csv(data_dir /'BTC_pro.csv', index_col=0)

feature_descriptions={
        'Open': 'Opening Price',
        'Close': 'Closing Price',
        'Low': 'Lowest Price',
        'High': 'Highest Price',
        'Volume': 'A measure of how much of a cryptocurrency was traded in the last 24 hours',
        'Market Cap': "The total market value of a cryptocurrency's circulating supply",
        'Return' : 'Return on the Single Day',
        'Cum_Return':'Cummulative Return',
        'Trend': 'Up or Down'}

Xr = btc.drop(columns=['Trend','Close','Cum_Return'], axis=1)
yr = btc['Close']

Xr_train = Xr.iloc[0:len(X)-30, :]
Xr_test= Xr.iloc[len(X)-30: , :]
yr_train = yr.iloc[0:len(X)-30]
yr_test = yr.iloc[len(X)-30:]

rfr = RandomForestRegressor()
rfr.fit(Xr_train,yr_train)
rfr_pred = rfr.predict(Xr_test)

explainer_r = RegressionExplainer(rfr, Xr_test, yr_test, X_background=Xr_train ,descriptions=feature_descriptions , 
                                  target='Close',units='$')

_ = ExplainerDashboard(explainer_r)
explainer_r.dump(pkl_dir /"explainer_r.joblib")
```
"""
                        ),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="reg-code-modal-close", className="ml-auto")
                        ),
                    ],
                    id="reg-code-modal",
                    size="lg",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)

default_cards = dbc.CardDeck([trend_card, price_card])
index_layout =  dbc.Container([
    navbar,     
    dbc.Row([
        dbc.Col([
            html.H3("explainerdashboard"),
           
        ])
    ]),
    
    
    dbc.Row([
        dbc.Col([
            html.H3("Bitcoin"),
            dcc.Markdown("""

"""),
        ])
    ]),
    
    dbc.Row([
        dbc.Col([
            default_cards,
        ]),
    ]),
])

def register_callbacks(app):
    @app.callback(
        Output("clas-code-modal", "is_open"),
        Input("clas-code-modal-open", "n_clicks"), 
        Input("clas-code-modal-close", "n_clicks"),
        State("clas-code-modal", "is_open"),
    )
    def toggle_modal(click_open, click_close, is_open):
        if click_open or click_close:
            return not is_open
        return is_open

    @app.callback(
        Output("reg-code-modal", "is_open"),
        Input("reg-code-modal-open", "n_clicks"), 
        Input("reg-code-modal-close", "n_clicks"),
        State("reg-code-modal", "is_open"),
    )
    def toggle_modal(click_open, click_close, is_open):
        if click_open or click_close:
            return not is_open
        return is_open
