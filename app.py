from flask import Flask, render_template, request, redirect
import pickle
from sklearn import *
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        row = []
        columns_list=(['OrganizationalUnitTypeDescription','SourceDescription','PeriodDescription',
        'AspectGroupDescription','FactorDescription','AspectDescription','UnitDescription', 
        'GEIDescription','EmitterGEIDescription','VendorName','ScopeDescription','BiogenicEmission',
         'Year','Month','sum_lag_1', 'sum_lag_2','sum_lag_4','sum_lag_6', 'mean_lag_1','mean_lag_2', 'mean_lag_4','mean_lag_6'])
        for column in columns_list:
             if column in ['sum_lag_1', 'sum_lag_2','sum_lag_4','sum_lag_6', 'mean_lag_1','mean_lag_2', 'mean_lag_4','mean_lag_6']:
                row.append(float(request.form[column]))
             else:
                row.append(int(request.form[column]))
        print(row)
        pickled_model = pickle.load(open('model2.pkl', 'rb'))
        prediction = pickled_model.predict([row])
        return render_template('index.html',prediction=prediction,row=row)
    else:
        row = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        return render_template('index.html',row=row)


if __name__ == '__main__':
    app.run(debug=True,port=3000)