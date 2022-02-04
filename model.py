
import numpy as np
import pandas as pd   

from sklearn.preprocessing import StandardScaler
import xgboost
from xgboost import XGBClassifier

data = pd.read_csv('heart_failure_clinical_records_dataset.csv')

y = data.iloc[:,-1]
X = data.iloc[:, 0:-1]

scale = StandardScaler()

X_train = scale.fit_transform(X)

XGmodel = xgboost.XGBRFClassifier(max_depth=3, random_state=1)
XGmodel.fit(X_train,y)

predictionMap = {0: 'Low chances of heart failure', 1: 'High Chances of heart failure'}

def predict(features):
    features = features.astype(np.float64)
    features = features.values.reshape(1,-1)
    test = scale.transform(features)
    answer = predictionMap[XGmodel.predict(test)[0]]
    return answer