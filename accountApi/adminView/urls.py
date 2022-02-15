from . import views
from django.urls import path

app_name = 'adminView'

urlpatterns = [
    path('', views.index, name='index'),
    #path('repos/', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
]