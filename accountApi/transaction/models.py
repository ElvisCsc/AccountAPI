from django.db import models
from account.models import Account
from user.models import User

# Create your models here.
class Transaction(models.Model):

    def __str__(self):
        return str(self.id)

    id = models.IntegerField(primary_key=True, unique=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, default=None, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True)
    action = models.CharField(max_length=200)
    amount = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)