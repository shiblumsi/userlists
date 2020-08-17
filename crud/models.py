from django.db import models

class Crud(models.Model):
    name = models.CharField(max_length=30, blank=True,null=True)
    address = models.CharField(max_length=100, blank=True,null=True)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name