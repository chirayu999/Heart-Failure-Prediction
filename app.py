import model
import numpy as np
import pandas as pd
from flask import Flask, request, render_template, jsonify


app = Flask(__name__, template_folder="web_pages")


@app.route('/') 
def home():
    return render_template('index.html')


@app.route('/classify', methods=['POST', 'GET'])
def classify_type():

    age = request.args.get('age')
    anaemia = request.form.get("Anaemia")
    cpk = request.args.get('CPK')
    diabetes = request.form.get("Diabetes")
    ef = request.args.get('EF')
    hbp = request.form.get("HBP")
    platelets = request.args.get('Platelets')
    srct = request.args.get('SRCT')
    srco = request.args.get('SRCO')
    gender = request.form.get("gender")
    smoke = request.form.get("Smoke")
    days = request.args.get('Days')

    features = pd.Series([age, anaemia, cpk, diabetes, ef,
                         hbp, platelets, srct, srco, gender, smoke, days])

    prediction = model.predict(features)

    return render_template('prediction.html', prediction=prediction)

if(__name__ == '__main__'):
    app.run(debug=True,host='0.0.0.0')
