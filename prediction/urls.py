from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('predict/HeartDisease/',views.predict_heart_disease, name='predict_heart_disease')
]