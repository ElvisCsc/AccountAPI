from django.urls import path
from .views import transaction_list, transaction_detail

app_name = 'transaction'

urlpatterns = [
    path('', transaction_list, name='transactions'),
    path('<int:pk>/', transaction_detail, name='detail')
]