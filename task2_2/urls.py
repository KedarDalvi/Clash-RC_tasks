from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('success/',views.success,name='success')

]