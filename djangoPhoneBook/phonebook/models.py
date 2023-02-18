from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    #TODO change to email field
    email = models.CharField(max_length=80, null=True)
    address = models.CharField(max_length=80, null=True)
    secondary_phone_number = models.CharField(max_length=80, null=True)
    job = models.CharField(max_length=20, null=True)
    middle_name = models.CharField(max_length=80, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}: {} <{}>'.format(self.first_name, self.last_name, self.phone_number, self.email)


class Tag(models.Model):
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.ManyToManyField(Contact)
