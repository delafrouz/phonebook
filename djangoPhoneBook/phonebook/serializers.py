from rest_framework import serializers
from django.contrib.auth.models import User

from djangoPhoneBook.phonebook.models import User, Contact, Tag


class UserSerializer(serializers.ModelSerializer):
    # contacts = serializers.PrimaryKeyRelatedField(many=True, queryset=Contact.objects.all())
    #
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'id', 'phone_number', 'email', 'address', 'secondary_phone_number',
                  'job', 'middle_name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
