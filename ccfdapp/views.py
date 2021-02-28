from django.shortcuts import render
import pickle
import pandas as pd
import numpy as np
# Create your views here.


def homeview(request):
    return render(request,'home.html')

def getPredictions(time,amount):
    model = pickle.load(open('CCFD_Model2.pkl','rb'))
    data = pd.read_csv('creditcard.csv.zip')
    pcacredit= data[(data['Time'] == float(time)) & (data['Amount'] == float(amount))]
    print(pcacredit)
    if len(pcacredit) == 0:
        return 'error'
    else:
        required = np.array(pcacredit)
        testData = required[0][:-1].reshape(1,-1)
        print(testData)
        #model.decision_function(testData)

        prediction = model.predict(testData)
        print(prediction)
        if (prediction == [1]):
            return 1
        elif (prediction == [0]):
            return 0
        else:
            return 'error'

def resultview(request):
    time =  request.GET['time']
    amount =  request.GET['amount']
    res = getPredictions(time,amount)
    return render(request,'result.html',{'result':res})