from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [
    path('setdataregister', views.SetDataRegister.as_view(), name='setdataregister'),
    path('setcoderegister', views.SetcodeRegister.as_view(), name='setcoderegister'),
]