from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>', views.ItemDetail, name='detail'),
    path('new/', views.NewItem, name='new'),
    path('browse/', views.browse, name='browse'),
    path('<int:pk>/update/', views.updateItem, name='update'),
    path('<int:pk>/delete', views.deleteItem, name="delete"),
]
