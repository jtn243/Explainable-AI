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
    brand="Titanic Explainer",
    brand_href="https://github.com/jtn243/Expalinable-AI",
    color="primary",
    dark=True,
    fluid=True,
)

trend_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Classifier Dashboard", className="card-title"),
                html.P(
                    "Predicting the probability of surviving "
                    "the titanic. Showing the full default dashboard."
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
from sklearn.ensemble import RandomForestClassifier
from explainerdashboard import ClassifierExplainer, ExplainerDashboard
from explainerdashboard.datasets import titanic_survive, feature_descriptions
X_train, y_train, X_test, y_test = titanic_survive()
model = RandomForestClassifier(n_estimators=50, max_depth=10).fit(X_train, y_train)
explainer = ClassifierExplainer(model, X_test, y_test, 
                               cats=['Sex', 'Deck', 'Embarked'],
                               descriptions=feature_descriptions,
                               labels=['Not survived', 'Survived'])
                               
ExplainerDashboard(explainer).run()
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
        dbc.CardBody(
            [
                html.H4("Regression Dashboard", className="card-title"),
                html.P(
                    "Predicting the fare paid for a ticket on the titanic. "
                    "Showing the full default dashboard."
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
from sklearn.ensemble import RandomForestRegressor
from explainerdashboard import RegressionExplainer, ExplainerDashboard
from explainerdashboard.datasets import titanic_fare, feature_descriptions
X_train, y_train, X_test, y_test = titanic_fare()
model = RandomForestRegressor(n_estimators=50, max_depth=10).fit(X_train, y_train)
explainer = RegressionExplainer(model, X_test, y_test, 
                                cats=['Sex', 'Deck', 'Embarked'], 
                                descriptions=feature_descriptions,
                                units="$")
                               
ExplainerDashboard(explainer).run()
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
#custom_cards = dbc.CardDeck([simple_survive_card, simple_ticket_card, custom_card])

index_layout =  dbc.Container([
    navbar,     
    dbc.Row([
        dbc.Col([
            html.H3("explainerdashboard"),
           
        ])
    ]),
    
    
    dbc.Row([
        dbc.Col([
            html.H3("Examples"),
            dcc.Markdown("""
Below you can find demonstrations of the three default dashboards for classification, 
regression and multi class classification problems, plus one demonstration of 
a custom dashboard.
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
