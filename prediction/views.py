from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls.resolvers import ResolverMatch
#from django.views.decorators.csrf import csrf_exempt
import joblib
import numpy as np
import urllib
#import cv2

#  first download the .h5 model file from github using the trick.

def home(request):
    return render(request, "prediction/home.html")

def predict_heart_disease(request):
    if request.method == 'POST':
        param = request.POST
        print(param)
        param = list(param.values())
        param = param[1:]
        print(param)
        param = np.array(param).reshape(1,7)
        model = joblib.load(r"E:\DiseasePrediction\prediction\models\heart_model.pkl")
        prediction = model.predict(param)
        print(prediction)
        # context={}
        #return HttpResponse(request,"You have chances of Heart Disease")
        if prediction[0] == 1:
            print("1")
            disease = "<html><h1>You have chances of Heart Disease</h1></html>"
            #context['has_disease']= disease
            #return render(request, "prediction/result.html", context={'has_disease':'You have chances of Heart Disease'})
            #return redirect('/home/')
            return HttpResponse(disease, content_type='text/plain')
        else:
            print("0")
            disease = "You don't have chances of Heart Disease"
            # context['no_disease'] = disease
            #return render(request, "prediction/result.html", context={'no_disease':disease})
            # return redirect('/')
            return HttpResponse(disease, content_type='text/plain')
    else:
        return render(request, 'prediction/heartdisease.html')


