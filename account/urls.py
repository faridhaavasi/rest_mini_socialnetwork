from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = 'account'
urlpatterns = [
    path('setdataregister', views.SetDataRegister.as_view(), name='setdataregister'),
    path('setcoderegister', views.SetcodeRegister.as_view(), name='setcoderegister'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

]