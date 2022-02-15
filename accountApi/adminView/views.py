from django.shortcuts import render
from account.models import Account
from user.models import User
from transaction.models import Transaction

# Create your views here.
def index(request):
    return render(request, 'adminView/index.html')

def detail(request, pk):
    user = User.objects.get(id=pk)
    accounts = Account.objects.filter(user=user)
    transactions = Transaction.objects.filter(user=user)
    context = {
        'user' : user,
        'accounts': accounts,
        'transactions' : transactions
    }
    return render(request, 'adminView/detail.html', context)

def csv(request):
    return render(request, 'adminView/index.html')