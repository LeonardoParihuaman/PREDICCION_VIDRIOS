import numpy as np
# from xgboost import XGBClassifier
# from sklearn.ensemble import XGBoost as xgb
# from xgboost.sklearn import XGBClassifier
import pickle
# from sklearn.externals import joblib       
from sklearn.ensemble import RandomForestClassifier
#import xgboost as xgb
import pandas as pd
from flask import Flask, request, render_template
# import joblib


app = Flask(__name__)
model = pickle.load(open('modelo.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST']) 
def predict():
    input_features = [float(x) for x in request.form.values()]

    features_value = [np.array(input_features)]
    
    features_name = ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']
    
    df = pd.DataFrame(features_value, columns=features_name)
    print(df)
    output = model.predict(df)
        
    if output == 1:
        res_val = "** building windows **"
    elif output == 2:
        res_val = "** no building windows **"
    elif output == 3:
        res_val = "** bheadlamp **"
    elif output == 4:
        res_val = "** vehicle building windows **"
    elif output == 5:
        res_val = "** Container **"
    elif output == 6:
        res_val = "** Tableware **"
    return render_template('index.html', prediction_text='EL vidiro es de tipo {}'.format(res_val))

if __name__ == "__main__":
#     app.debug = True
    app.run(host="0.0.0.0", port =5000)
