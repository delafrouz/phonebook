from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    user_id = models.IntegerField(primary_key=True)


class Contact(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    id = models.IntegerField(primary_key=True)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    secondary_phone_number = models.CharField(max_length=80)
    job = models.CharField(max_length=20)
