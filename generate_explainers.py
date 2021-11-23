import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import math
import warnings

pkl_dir = Path.cwd() / "pkls"
data_dir= Path.cwd() / "data"

btc = pd.read_csv(data_dir /'BTC_pro.csv')

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

from imblearn.over_sampling import SMOTE
oversample = SMOTE()
X_train,y_train = oversample.fit_resample(X_train,y_train)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_curve
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
rfc = RandomForestClassifier()
rfc.fit(X_train,y_train)
rfc_pred = rfc.predict(X_test)

Xr = btc.drop(columns=['Trend','Close','Cum_Return'], axis=1)
yr = btc['Close']

Xr_train = Xr.iloc[0:len(X)-30, :]
Xr_test= Xr.iloc[len(X)-30: , :]
yr_train = yr.iloc[0:len(X)-30]
yr_test = yr.iloc[len(X)-30:]

from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor()
rfr.fit(Xr_train,yr_train)
rfr_pred = rfr.predict(Xr_test)

from explainerdashboard import ClassifierExplainer, RegressionExplainer, ExplainerDashboard, ExplainerHub


explainer_r = RegressionExplainer(rfr, Xr_test, yr_test, X_background=Xr_train ,descriptions=feature_descriptions , 
                                  target='Close',units='$')

#explainer_r = ExplainerDashboard(explainer_r, title='Regression Explainer')
_ = ExplainerDashboard(explainer_r)
explainer_r.dump(pkl_dir /"explainer_r.pkl")


explainer_c = ClassifierExplainer(rfc, X_test, y_test, X_background=X_train,descriptions=feature_descriptions , 
                                  target='Trend', labels=['Down','Up'])
_ = ExplainerDashboard(explainer_c)
explainer_c.dump(pkl_dir /"explainer_c.pkl")



