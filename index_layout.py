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
        dbc.CardImg(src="assets/btc_trend.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Classifier Dashboard", className="card-title"),
                html.P(
                    "Predicting the Trend of Bitcoin for last 30 Days"
                    ,className="card-text",
                ),
                html.A(dbc.Button("Go to dashboard", color="primary"),
                       href="/btc_classifier"),
                dbc.Button("Show Code", id="clas-code-modal-open", className="mr-1"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Code needed for this Classifier Dashboard"),
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
        'Cum_Return':'Cumulative Return',
        'Trend': 'Up or Down'}

X = btc.drop(columns=['Trend','Return'], axis=1)
y = btc['Trend']

X_train = X.iloc[0:len(X)-30, :]
X_test= X.iloc[len(X)-30: , :]
y_train = y.iloc[0:len(X)-30]
y_test = y.iloc[len(X)-30:]

rfc = RandomForestClassifier()
rfc.fit(X_train,y_train)
rfc_pred = rfc.predict(X_test)

explainer_c = ClassifierExplainer(rfc, X_test, y_test,descriptions=feature_descriptions , 
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
        dbc.CardImg(src="assets/btc_price.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Regression Dashboard", className="card-title"),
                html.P(
                    "Predicting the Close Price of Bitcoin for last 30 Days"
                    ,className="card-text",
                ),
                html.A(dbc.Button("Go to dashboard", color="primary"),
                       href="/btc_regression"),
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
        'Cum_Return':'Cumulative Return',
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

etht_card = dbc.Card(
    [
        dbc.CardImg(src="assets/eth_trend.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Classifier Dashboard", className="card-title"),
                html.P(
                    "Predicting the Trend of ETH for last 30 Days"
                    ,className="card-text",
                ),
                html.A(dbc.Button("Go to dashboard", color="primary"),
                       href="/eth_classifier"),
                dbc.Button("Show Code", id="cleth-code-modal-open", className="mr-1"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Code needed for this Classifier Dashboard"),
                        dcc.Markdown(
"""
```python
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard


pkl_dir = Path.cwd() / "pkls"
data_dir= Path.cwd() / "data"

eth = pd.read_csv(data_dir /'ETH_pro.csv', index_col=0)

feature_descriptions={
        'Open': 'Opening Price',
        'Close': 'Closing Price',
        'Low': 'Lowest Price',
        'High': 'Highest Price',
        'Volume': 'A measure of how much of a cryptocurrency was traded in the last 24 hours',
        'Market Cap': "The total market value of a cryptocurrency's circulating supply",
        'Return' : 'Return on the Single Day',
        'Cum_Return':'Cumulative Return',
        'Trend': 'Up or Down'}

X = eth.drop(columns=['Trend','Return'], axis=1)
y = eth['Trend']

X_train = X.iloc[0:len(X)-30, :]
X_test= X.iloc[len(X)-30: , :]
y_train = y.iloc[0:len(X)-30]
y_test = y.iloc[len(X)-30:]

rfc = RandomForestClassifier()
rfc.fit(X_train,y_train)
rfc_pred = rfc.predict(X_test)

explainer_c = ClassifierExplainer(rfc, X_test, y_test,descriptions=feature_descriptions , 
                                  target='Trend', labels=['Down','Up'])
_ = ExplainerDashboard(explainer_c)
explainer_c.dump(pkl_dir /"explainer_c.joblib")
```
"""
                        ),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="cleth-code-modal-close", className="ml-auto")
                        ),
                    ],
                    id="cleth-code-modal",
                    size="lg",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)

ethp_card = dbc.Card(
    [
        dbc.CardImg(src="assets/eth_price.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Regression Dashboard", className="card-title"),
                html.P(
                    "Predicting the Close Price of ETH for last 30 Days"
                    ,className="card-text",
                ),
                html.A(dbc.Button("Go to dashboard", color="primary"),
                       href="/eth_regression"),
                dbc.Button("Show Code", id="rgeth-code-modal-open", className="mr-1"),
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

eth = pd.read_csv(data_dir /'ETH_pro.csv', index_col=0)

feature_descriptions={
        'Open': 'Opening Price',
        'Close': 'Closing Price',
        'Low': 'Lowest Price',
        'High': 'Highest Price',
        'Volume': 'A measure of how much of a cryptocurrency was traded in the last 24 hours',
        'Market Cap': "The total market value of a cryptocurrency's circulating supply",
        'Return' : 'Return on the Single Day',
        'Cum_Return':'Cumulative Return',
        'Trend': 'Up or Down'}

Xr = eth.drop(columns=['Trend','Close','Cum_Return'], axis=1)
yr = eth['Close']

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
                            dbc.Button("Close", id="rgeth-code-modal-close", className="ml-auto")
                        ),
                    ],
                    id="rgeth-code-modal",
                    size="lg",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)

adat_card = dbc.Card(
    [
        dbc.CardImg(src="assets/ada_trend.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Classifier Dashboard", className="card-title"),
                html.P(
                    "Predicting the Trend of ADA for last 30 Days"
                    ,className="card-text",
                ),
                html.A(dbc.Button("Go to dashboard", color="primary"),
                       href="/ada_classifier"),
                dbc.Button("Show Code", id="clada-code-modal-open", className="mr-1"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Code needed for this Classifier Dashboard"),
                        dcc.Markdown(
"""
```python
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard


pkl_dir = Path.cwd() / "pkls"
data_dir= Path.cwd() / "data"

ada = pd.read_csv(data_dir /'ADA_pro.csv', index_col=0)

feature_descriptions={
        'Open': 'Opening Price',
        'Close': 'Closing Price',
        'Low': 'Lowest Price',
        'High': 'Highest Price',
        'Volume': 'A measure of how much of a cryptocurrency was traded in the last 24 hours',
        'Market Cap': "The total market value of a cryptocurrency's circulating supply",
        'Return' : 'Return on the Single Day',
        'Cum_Return':'Cumulative Return',
        'Trend': 'Up or Down'}

X = ada.drop(columns=['Trend','Return'], axis=1)
y = ada['Trend']

X_train = X.iloc[0:len(X)-30, :]
X_test= X.iloc[len(X)-30: , :]
y_train = y.iloc[0:len(X)-30]
y_test = y.iloc[len(X)-30:]

rfc = RandomForestClassifier()
rfc.fit(X_train,y_train)
rfc_pred = rfc.predict(X_test)

explainer_c = ClassifierExplainer(rfc, X_test, y_test, descriptions=feature_descriptions , 
                                  target='Trend', labels=['Down','Up'])
_ = ExplainerDashboard(explainer_c)
explainer_c.dump(pkl_dir /"explainer_c.joblib")
```
"""
                        ),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="clada-code-modal-close", className="ml-auto")
                        ),
                    ],
                    id="clada-code-modal",
                    size="lg",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)

adap_card = dbc.Card(
    [
        dbc.CardImg(src="assets/ada_price.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Regression Dashboard", className="card-title"),
                html.P(
                    "Predicting the Close Price of ADA for last 30 Days"
                    ,className="card-text",
                ),
                html.A(dbc.Button("Go to dashboard", color="primary"),
                       href="/ada_regression"),
                dbc.Button("Show Code", id="rgada-code-modal-open", className="mr-1"),
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

ada = pd.read_csv(data_dir /'ADA_pro.csv', index_col=0)

feature_descriptions={
        'Open': 'Opening Price',
        'Close': 'Closing Price',
        'Low': 'Lowest Price',
        'High': 'Highest Price',
        'Volume': 'A measure of how much of a cryptocurrency was traded in the last 24 hours',
        'Market Cap': "The total market value of a cryptocurrency's circulating supply",
        'Return' : 'Return on the Single Day',
        'Cum_Return':'Cumulative Return',
        'Trend': 'Up or Down'}

Xr = ada.drop(columns=['Trend','Close','Cum_Return'], axis=1)
yr = ada['Close']

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
                            dbc.Button("Close", id="rgada-code-modal-close", className="ml-auto")
                        ),
                    ],
                    id="rgada-code-modal",
                    size="lg",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)

bnbt_card = dbc.Card(
    [
        dbc.CardImg(src="assets/bnb_trend.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Classifier Dashboard", className="card-title"),
                html.P(
                    "Predicting the Trend of BNB for last 30 Days"
                    ,className="card-text",
                ),
                html.A(dbc.Button("Go to dashboard", color="primary"),
                       href="/bnb_classifier"),
                dbc.Button("Show Code", id="clbnb-code-modal-open", className="mr-1"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Code needed for this Classifier Dashboard"),
                        dcc.Markdown(
"""
```python
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard


pkl_dir = Path.cwd() / "pkls"
data_dir= Path.cwd() / "data"

bnb = pd.read_csv(data_dir /'BNB_pro.csv', index_col=0)

feature_descriptions={
        'Open': 'Opening Price',
        'Close': 'Closing Price',
        'Low': 'Lowest Price',
        'High': 'Highest Price',
        'Volume': 'A measure of how much of a cryptocurrency was traded in the last 24 hours',
        'Market Cap': "The total market value of a cryptocurrency's circulating supply",
        'Return' : 'Return on the Single Day',
        'Cum_Return':'Cumulative Return',
        'Trend': 'Up or Down'}

X = bnb.drop(columns=['Trend','Return'], axis=1)
y = bnb['Trend']

X_train = X.iloc[0:len(X)-30, :]
X_test= X.iloc[len(X)-30: , :]
y_train = y.iloc[0:len(X)-30]
y_test = y.iloc[len(X)-30:]

rfc = RandomForestClassifier()
rfc.fit(X_train,y_train)
rfc_pred = rfc.predict(X_test)

explainer_c = ClassifierExplainer(rfc, X_test, y_test, descriptions=feature_descriptions , 
                                  target='Trend', labels=['Down','Up'])
_ = ExplainerDashboard(explainer_c)
explainer_c.dump(pkl_dir /"explainer_c.joblib")
```
"""
                        ),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="clbnb-code-modal-close", className="ml-auto")
                        ),
                    ],
                    id="clbnb-code-modal",
                    size="lg",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)

bnbp_card = dbc.Card(
    [
        dbc.CardImg(src="assets/bnb_trend.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Regression Dashboard", className="card-title"),
                html.P(
                    "Predicting the Close Price of BNB for last 30 Days"
                    ,className="card-text",
                ),
                html.A(dbc.Button("Go to dashboard", color="primary"),
                       href="/bnb_regression"),
                dbc.Button("Show Code", id="rgbnb-code-modal-open", className="mr-1"),
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

bnb = pd.read_csv(data_dir /'BNB_pro.csv', index_col=0)

feature_descriptions={
        'Open': 'Opening Price',
        'Close': 'Closing Price',
        'Low': 'Lowest Price',
        'High': 'Highest Price',
        'Volume': 'A measure of how much of a cryptocurrency was traded in the last 24 hours',
        'Market Cap': "The total market value of a cryptocurrency's circulating supply",
        'Return' : 'Return on the Single Day',
        'Cum_Return':'Cumulative Return',
        'Trend': 'Up or Down'}

Xr = bnb.drop(columns=['Trend','Close','Cum_Return','Market Cap'], axis=1)
yr = bnb['Close']

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
                            dbc.Button("Close", id="rgbnb-code-modal-close", className="ml-auto")
                        ),
                    ],
                    id="rgbnb-code-modal",
                    size="lg",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)

xrpt_card = dbc.Card(
    [
        dbc.CardImg(src="assets/xrp_trend.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Classifier Dashboard", className="card-title"),
                html.P(
                    "Predicting the Trend of XRP for last 30 Days"
                    ,className="card-text",
                ),
                html.A(dbc.Button("Go to dashboard", color="primary"),
                       href="/xrp_classifier"),
                dbc.Button("Show Code", id="clxrp-code-modal-open", className="mr-1"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Code needed for this Classifier Dashboard"),
                        dcc.Markdown(
"""
```python
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard


pkl_dir = Path.cwd() / "pkls"
data_dir= Path.cwd() / "data"

xrp = pd.read_csv(data_dir /'XRP_pro.csv', index_col=0)

feature_descriptions={
        'Open': 'Opening Price',
        'Close': 'Closing Price',
        'Low': 'Lowest Price',
        'High': 'Highest Price',
        'Volume': 'A measure of how much of a cryptocurrency was traded in the last 24 hours',
        'Market Cap': "The total market value of a cryptocurrency's circulating supply",
        'Return' : 'Return on the Single Day',
        'Cum_Return':'Cumulative Return',
        'Trend': 'Up or Down'}

X = xrp.drop(columns=['Trend','Return'], axis=1)
y = xrp['Trend']

X_train = X.iloc[0:len(X)-30, :]
X_test= X.iloc[len(X)-30: , :]
y_train = y.iloc[0:len(X)-30]
y_test = y.iloc[len(X)-30:]

rfc = RandomForestClassifier()
rfc.fit(X_train,y_train)
rfc_pred = rfc.predict(X_test)

explainer_c = ClassifierExplainer(rfc, X_test, y_test,descriptions=feature_descriptions , 
                                  target='Trend', labels=['Down','Up'])
_ = ExplainerDashboard(explainer_c)
explainer_c.dump(pkl_dir /"explainer_c.joblib")
```
"""
                        ),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="clxrp-code-modal-close", className="ml-auto")
                        ),
                    ],
                    id="clxrp-code-modal",
                    size="lg",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)

xrpp_card = dbc.Card(
    [
        dbc.CardImg(src="assets/xrp_trend.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Regression Dashboard", className="card-title"),
                html.P(
                    "Predicting the Close Price of XRP for last 30 Days"
                    ,className="card-text",
                ),
                html.A(dbc.Button("Go to dashboard", color="primary"),
                       href="/xrp_regression"),
                dbc.Button("Show Code", id="rgxrp-code-modal-open", className="mr-1"),
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

xrp = pd.read_csv(data_dir /'XRP_pro.csv', index_col=0)

feature_descriptions={
        'Open': 'Opening Price',
        'Close': 'Closing Price',
        'Low': 'Lowest Price',
        'High': 'Highest Price',
        'Volume': 'A measure of how much of a cryptocurrency was traded in the last 24 hours',
        'Market Cap': "The total market value of a cryptocurrency's circulating supply",
        'Return' : 'Return on the Single Day',
        'Cum_Return':'Cumulative Return',
        'Trend': 'Up or Down'}

Xr = xrp.drop(columns=['Trend','Close','Cum_Return'], axis=1)
yr = xrp['Close']

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
                            dbc.Button("Close", id="rgxrp-code-modal-close", className="ml-auto")
                        ),
                    ],
                    id="rgxrp-code-modal",
                    size="lg",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},
)



btc_cards = dbc.CardDeck([trend_card, price_card])
eth_cards = dbc.CardDeck([etht_card, ethp_card])
ada_cards = dbc.CardDeck([adat_card, adap_card])
bnb_cards = dbc.CardDeck([bnbt_card, bnbp_card])
xrp_cards = dbc.CardDeck([xrpt_card, xrpp_card])


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
            btc_cards,
        ]),
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("Ethereum"),
        ])
    ]),
    
    dbc.Row([
        dbc.Col([
            eth_cards,
        ]),
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("Cardano"),
        ])
    ]),
    
    dbc.Row([
        dbc.Col([
            ada_cards,
        ]),
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("Binance Coin"),
        ])
    ]),
    
    dbc.Row([
        dbc.Col([
            bnb_cards,
        ]),
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("XRP"),
        ])
    ]),
    
    dbc.Row([
        dbc.Col([
            xrp_cards,
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
    
    @app.callback(
        Output("cleth-code-modal", "is_open"),
        Input("cleth-code-modal-open", "n_clicks"), 
        Input("cleth-code-modal-close", "n_clicks"),
        State("cleth-code-modal", "is_open"),
    )
    def toggle_modal(click_open, click_close, is_open):
        if click_open or click_close:
            return not is_open
        return is_open

    @app.callback(
        Output("rgeth-code-modal", "is_open"),
        Input("rgeth-code-modal-open", "n_clicks"), 
        Input("rgeth-code-modal-close", "n_clicks"),
        State("rgeth-code-modal", "is_open"),
    )
    def toggle_modal(click_open, click_close, is_open):
        if click_open or click_close:
            return not is_open
        return is_open
    
    @app.callback(
        Output("clada-code-modal", "is_open"),
        Input("clada-code-modal-open", "n_clicks"), 
        Input("clada-code-modal-close", "n_clicks"),
        State("clada-code-modal", "is_open"),
    )
    def toggle_modal(click_open, click_close, is_open):
        if click_open or click_close:
            return not is_open
        return is_open

    @app.callback(
        Output("rgada-code-modal", "is_open"),
        Input("rgada-code-modal-open", "n_clicks"), 
        Input("rgada-code-modal-close", "n_clicks"),
        State("rgada-code-modal", "is_open"),
    )
    def toggle_modal(click_open, click_close, is_open):
        if click_open or click_close:
            return not is_open
        return is_open
    
    @app.callback(
        Output("clbnb-code-modal", "is_open"),
        Input("clbnb-code-modal-open", "n_clicks"), 
        Input("clbnb-code-modal-close", "n_clicks"),
        State("clbnb-code-modal", "is_open"),
    )
    def toggle_modal(click_open, click_close, is_open):
        if click_open or click_close:
            return not is_open
        return is_open

    @app.callback(
        Output("rgbnb-code-modal", "is_open"),
        Input("rgbnb-code-modal-open", "n_clicks"), 
        Input("rgbnb-code-modal-close", "n_clicks"),
        State("rgbnb-code-modal", "is_open"),
    )
    def toggle_modal(click_open, click_close, is_open):
        if click_open or click_close:
            return not is_open
        return is_open
    
    @app.callback(
        Output("clxrp-code-modal", "is_open"),
        Input("clxrp-code-modal-open", "n_clicks"), 
        Input("clxrp-code-modal-close", "n_clicks"),
        State("clxrp-code-modal", "is_open"),
    )
    def toggle_modal(click_open, click_close, is_open):
        if click_open or click_close:
            return not is_open
        return is_open

    @app.callback(
        Output("rgxrp-code-modal", "is_open"),
        Input("rgxrp-code-modal-open", "n_clicks"), 
        Input("rgxrp-code-modal-close", "n_clicks"),
        State("rgxrp-code-modal", "is_open"),
    )
    def toggle_modal(click_open, click_close, is_open):
        if click_open or click_close:
            return not is_open
        return is_open
    
    
