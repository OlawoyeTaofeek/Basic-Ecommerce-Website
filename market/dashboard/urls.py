from django.urls import path

from . import views

app_name = 'dashbord'

urlpatterns = [
    path('dashbord', views.Index, name='Index'),
]
