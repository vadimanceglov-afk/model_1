from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length = 20)


class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
