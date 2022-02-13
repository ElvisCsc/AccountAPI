from django.db import models
from account.models import Account
from user.models import User

# Create your models here.
class Transaction(models.Model):

    def __str__(self):
        return self.id

    id = models.IntegerField(primary_key=True, unique=True)
    account = models.ForeignKey(Account, default=None)
    user = models.ForeignKey(User)
    action = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)