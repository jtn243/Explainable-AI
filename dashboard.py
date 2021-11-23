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
from custom import CustomModelTab, CustomPredictionsTab

pkl_dir = Path.cwd() / "pkls"

app = Flask(__name__)

explainer_c = ClassifierExplainer.from_file(pkl_dir / "explainer_c.joblib")
clas_dashboard = ExplainerDashboard(explainer_c, 
                    title="Classifier Explainer: Predicting survival on the Titanic", 
                    server=app, url_base_pathname="/classifier/", 
                    header_hide_selector=True)

explainer_r = RegressionExplainer.from_file(pkl_dir / "explainer_r.joblib")
reg_dashboard = ExplainerDashboard(explainer_r, 
                    title="Regression Explainer: Predicting ticket fare",
                    server=app, url_base_pathname="/regression/")


index_app = dash.Dash(
    __name__, 
    server=app, 
    url_base_pathname="/", 
    external_stylesheets=[BOOTSTRAP])

index_app.title = 'explainerdashboard'
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
