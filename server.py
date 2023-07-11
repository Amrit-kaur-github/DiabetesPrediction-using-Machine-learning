from flask import *

import numpy

import pandas as pd

from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


app=Flask(__name__)

  
#DIABETES PREDICTION
@app.route('/')
def heartpage():
    return render_template("diabetes.html")
  
# AGE: The age of the patient.
# PREGNANCIES: The number of times the patient has been pregnant.
# GLUCOSE: The plasma glucose concentration in a 2-hour oral glucose tolerance test.
# BLOODPRESSURE: The diastolic blood pressure (mm Hg).
# SKINTHICKNESS: The thickness of the skinfold at the triceps (mm).
# INSULIN: The 2-hour serum insulin level (mu U/ml).
# BMI: The body mass index (weight in kg / (height in m)^2).
# DIABETESPEDIGREEFUNCTION: The diabetes pedigree function, which provides information about 
# the genetic influence of diabetes among relatives.


@app.route('/diabetess', methods=["POST"])
def prediction():
  AGE=eval(request.form.get("AGE"))
  PREGNANCIES=int(request.form.get("PREGNANCIES"))
  GLUCOSE=int(request.form.get("GLUCOSE"))
  BLOODPRESSURE=eval(request.form.get("BLOODPRESSURE"))
  SKINTHICKNESS=eval(request.form.get("SKINTHICKNESS"))
  INSULIN=int(request.form.get("INSULIN"))
  BMI=float(request.form.get("BMI"))
  DIABETES_PEDIGREE_FUNCTION=float(request.form.get("DIABETES_PEDIGREE_FUNCTION"))
  
  csv="diabetes.csv"
  data=pd.read_csv(csv)
  data=data.values
  x=data[:,:8]
  y=data[:,-1]

  model=GaussianNB()
  model.fit(x,y)
  
  prediction=model.predict([[PREGNANCIES,GLUCOSE,BLOODPRESSURE,SKINTHICKNESS,INSULIN,BMI,DIABETES_PEDIGREE_FUNCTION,AGE]])
  
  return render_template("diabetes.html",data=prediction[0])


if __name__ == '__main__':
  app.run()