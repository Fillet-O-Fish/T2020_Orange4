from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=60)
    userid = models.CharField(max_length=60)
    creditAccList = models.CharField(max_length=60)
    depositAccList = models.CharField(max_length=60)
    def __str__(self):
        return self.name