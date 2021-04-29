from django.shortcuts import render
from django.http import HttpResponse
import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

model=joblib.load('./models/diabetes.pickle')
# Create your views here.



def predict(request):
    
    if request.method == 'POST': 
        
        temp={}
        
        temp['Pregnancies']=float(request.POST.get('Pregnancies'))
        temp['Glucose']=float(request.POST.get('Glucose'))
        temp['BloodPressure'] =float(request.POST.get('BloodPressure'))
        temp['SkinThickness']= float(request.POST.get('SkinThickness'))
        temp['Insulin']= float(request.POST.get('Insulin'))
        temp['BMI'] =float(request.POST.get('BMI'))
        temp['DiabetesPedigreeFunction'] = float( request.POST.get('DiabetesPedigreeFunction'))
        temp['Age'] = float(request.POST.get('Age'))
        
        testdata = pd.DataFrame({'x': temp}).transpose()
       
        result=model.predict(testdata)[0]
        print(result)
       
        context={'result':result}

        return render(request,'predict.html',context)
    else:
        return render(request, 'predict.html')

