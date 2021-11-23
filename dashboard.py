from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard, ExplainerHub
# you can override params during load from_config:
db = ExplainerDashboard.from_config("dashboard.yaml", title="Awesomer Title")

app = db.flask_server()
