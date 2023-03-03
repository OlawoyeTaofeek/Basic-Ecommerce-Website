from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import IndexView
from .forms import LoginForm

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', views.contactView, name='contact'),
    path('signup', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name ='core/index.html'), name ='logout'),
]
