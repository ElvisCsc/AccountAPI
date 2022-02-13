from django.db import models
from user.models import User

# Create your models here.
class Account(models.Model):

    def __str__(self):
        return self.id

    id = models.IntegerField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    type = models.CharField(max_length=10, default=None, unique=True)
    amount = models.DecimalField(default=0, decimal_places=2)
    
