from rest_framework import serializers

from djangoPhoneBook.phonebook.models import User, Contact


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'id']


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'id', 'phone_number', 'email', 'address', 'secondary_phone_number',
                  'job', 'middle_name']
