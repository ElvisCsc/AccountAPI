from django.shortcuts import render
from account.models import Account
from user.models import User
from transaction.models import Transaction

# Create your views here.
def homebase(request):
    return render(request, 'jkjkl')