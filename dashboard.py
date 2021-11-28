# xgboost is a dependency of dtreeviz, but too large (>350M) for heroku
# so we uninstall it and mock it here:
from unittest.mock import MagicMock
import sys
sys.modules["xgboost"] = MagicMock()

from pathlib import Path
from flask import Flask

import dash
from dash_bootstrap_components.themes import FLATLY, BOOTSTRAP # bootstrap theme
from explainerdashboard import *

from index_layout import index_layout, register_callbacks
#from custom import CustomModelTab, CustomPredictionsTab

pkl_dir = Path.cwd() / "pkls"

app = Flask(__name__)

explainer_c = ClassifierExplainer.from_file(pkl_dir / "explainer_c.joblib")
clas_dashboard = ExplainerDashboard(explainer_c, 
                    title="Classifier Explainer: Trend Prediction", 
                    server=app, url_base_pathname="/classifier/", 
                    header_hide_selector=True)

explainer_r = RegressionExplainer.from_file(pkl_dir / "explainer_r.joblib")
reg_dashboard = ExplainerDashboard(explainer_r, 
                    title="Regression Explainer: Close Price Prediction",
                    server=app, url_base_pathname="/regression/")

explainer_ceth = ClassifierExplainer.from_file(pkl_dir / "explainer_ceth.joblib")
cleth_dashboard = ExplainerDashboard(explainer_ceth, 
                    title="Classifier Explainer: Trend Prediction", 
                    server=app, url_base_pathname="/eth_classifier/", 
                    header_hide_selector=True)

explainer_reth = RegressionExplainer.from_file(pkl_dir / "explainer_reth.joblib")
rgeth_dashboard = ExplainerDashboard(explainer_reth, 
                    title="Regression Explainer: Close Price Prediction",
                    server=app, url_base_pathname="/eth_regression/")

explainer_cada = ClassifierExplainer.from_file(pkl_dir / "explainer_cada.joblib")
clada_dashboard = ExplainerDashboard(explainer_cada, 
                    title="Classifier Explainer: Trend Prediction", 
                    server=app, url_base_pathname="/ada_classifier/", 
                    header_hide_selector=True)

explainer_rada = RegressionExplainer.from_file(pkl_dir / "explainer_rada.joblib")
rgada_dashboard = ExplainerDashboard(explainer_rada, 
                    title="Regression Explainer: Close Price Prediction",
                    server=app, url_base_pathname="/ada_regression/")

explainer_cbnb = ClassifierExplainer.from_file(pkl_dir / "explainer_cbnb.joblib")
clbnb_dashboard = ExplainerDashboard(explainer_cbnb, 
                    title="Classifier Explainer: Trend Prediction", 
                    server=app, url_base_pathname="/bnb_classifier/", 
                    header_hide_selector=True)

explainer_rbnb = RegressionExplainer.from_file(pkl_dir / "explainer_rbnb.joblib")
rgbnb_dashboard = ExplainerDashboard(explainer_rbnb, 
                    title="Regression Explainer: Close Price Prediction",
                    server=app, url_base_pathname="/bnb_regression/")

explainer_cxrp = ClassifierExplainer.from_file(pkl_dir / "explainer_cxrp.joblib")
clxrp_dashboard = ExplainerDashboard(explainer_cxrp, 
                    title="Classifier Explainer: Trend Prediction", 
                    server=app, url_base_pathname="/xrp_classifier/", 
                    header_hide_selector=True)

explainer_rxrp = RegressionExplainer.from_file(pkl_dir / "explainer_rxrp.joblib")
rgxrp_dashboard = ExplainerDashboard(explainer_rxrp, 
                    title="Regression Explainer: Close Price Prediction",
                    server=app, url_base_pathname="/xrp_regression/")


index_app = dash.Dash(
    __name__, 
    server=app, 
    url_base_pathname="/", 
    external_stylesheets=[BOOTSTRAP])

index_app.title = 'Bitcoin'
index_app.layout = index_layout
register_callbacks(index_app)

@app.route("/")
def index():
    return index_app.index()

@app.route('/classifier')
def classifier_dashboard():
    return clas_dashboard.app.index()

@app.route('/regression')
def regression_dashboard():
    return reg_dashboard.app.index()
  
@app.route('/eth_classifier')
def cleth_dashboard():
    return cleth_dashboard.app.index()

@app.route('/eth_regression')
def rgeth_dashboard():
    return rgeth_dashboard.app.index()
  
@app.route('/ada_classifier')
def clada_dashboard():
    return clada_dashboard.app.index()

@app.route('/ada_regression')
def rgada_dashboard():
    return rgada_dashboard.app.index()
  
@app.route('/bnb_classifier')
def clbnb_dashboard():
    return clbnb_dashboard.app.index()

@app.route('/bnb_regression')
def rgbnb_dashboard():
    return rgbnb_dashboard.app.index()
  
@app.route('/xrp_classifier')
def clxrp_dashboard():
    return clxrp_dashboard.app.index()

@app.route('/xrp_regression')
def rgxrp_dashboard():
    return rgxrp_dashboard.app.index()
