from django.urls import path
from .views import account_list, account_detail

app_name = 'account'

urlpatterns = [
    path('', account_list, name='account'),
    path('<int:pk>/', account_detail, name='detail')
]