from rest_framework import serializers
from django.contrib.auth.models import User

from djangoPhoneBook.phonebook.models import Contact, Tag


class UserSerializer(serializers.ModelSerializer):
    contacts = serializers.PrimaryKeyRelatedField(many=True, queryset=Contact.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'contacts', 'tags']


class ContactSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'id', 'phone_number', 'email', 'address', 'secondary_phone_number',
                  'job', 'middle_name', 'user']


class TagSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Tag
        fields = '__all__'
