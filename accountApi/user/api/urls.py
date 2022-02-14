from django.urls import path
from .views import user_list, user_detail

app_name = 'user'

urlpatterns = [
    path('', user_list, name='users'),
    path('<int:pk>/', user_detail, name='detail')
]