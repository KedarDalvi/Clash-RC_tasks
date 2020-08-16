from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="task1-home"),   
    path('about/',views.about, name="task1-about"),
    path('case/',views.case,name=" case-1")

    
]
