from . import views
from django.urls import path

app_name = 'adminView'

urlpatterns = [
    path('', views.homebase, name='base'),
    #path('repos/', views.index, name='index'),
    #path('repo/<int:repo_id>/', views.repoDetail, name='detail'),
]