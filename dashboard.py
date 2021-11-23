from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard, ExplainerHub
# you can override params during load from_config:
db1 = ExplainerDashboard.from_config("dashboard.yaml", title="Awesomer Title")

app = db1.flask_server()
