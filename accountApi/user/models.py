from django.db import models

# Create your models here.
class User(models.Model):

    def __str__(self):
        return self.name

    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)