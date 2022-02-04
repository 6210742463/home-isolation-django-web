from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('success/', success, name='success'),
    path('petient/', petient, name='petient'),
    path('doctor/', doctor, name='doctor'),
    path('history/<int:id>/', history, name='history'),
    path('dairy-pulse/', dairy_pulse, name='dairypulse'),
    path('send-pulse/', sendpulse, name='sendpulse'),
    path('reserve/', reserve, name='reserve'),
    path('success-reserve/', s_reserve, name='s_reserve'),
    path('petient-list/', petient_list, name='petient_list'),
]