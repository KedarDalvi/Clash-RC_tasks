from django.urls import path
from . import views

urlpatterns = [
    path('',views.home1, name="task2-home1"),   
    path('login1/',views.login1, name="task1-login1"),


    
]
