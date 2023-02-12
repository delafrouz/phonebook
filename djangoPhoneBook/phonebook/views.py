from django.http import HttpResponse, JsonResponse
from .models import User, Contact
from .serializers import UserSerializer, ContactSerializer
from rest_framework.decorators import api_view
from rest_framework.request import Request


class PhonebookView:
    @staticmethod
    @api_view(['GET'])
    def view_all_phonebook(request: Request):
        all_users = User.get_all_users()
        user_serializer = UserSerializer(all_users, many=True)
        return JsonResponse({'phonebook_users': user_serializer.data})

    @staticmethod
    def view_user_phonebook(request: Request, user_id: int):
        # TODO get one users contacts
        return HttpResponse('this is one persons phonebook at id={}'.format(user_id))


class UserView:
    @staticmethod
    @api_view(['GET', 'DELETE', 'PUT'])
    def view_profile_by_id(request: Request, user_id) -> JsonResponse:
        if request.method == 'GET':
            return UserView.get_user(user_id)
        if request.method == 'PUT':
            return UserView.update_user(user_id, request.data)
        if request.method == 'DELETE':
            return UserView.delete_user(user_id)

    @staticmethod
    @api_view(['POST'])
    def view_profile(request: Request) -> JsonResponse:
        if request.method == 'POST':
            return UserView.add_user(request.data)

    @staticmethod
    def get_user(user_id: int) -> JsonResponse:
        user = User.get_user(user_id)
        user_serializer = UserSerializer(user)
        return JsonResponse({'user': user_serializer.data})

    @staticmethod
    def update_user(user_id: int, data: dict) -> JsonResponse:
        user = User.update_user(user_id, data)
        user_serializer = UserSerializer(user)
        return JsonResponse({'user': user_serializer.data})

    @staticmethod
    def delete_user(user_id: int) -> JsonResponse:
        user = User.delete_user(user_id)
        user_serializer = UserSerializer(user)
        return JsonResponse({'user': user_serializer.data})

    @staticmethod
    def add_user(data: dict) -> JsonResponse:
        user = User.add_user(data)
        user_serializer = UserSerializer(user)
        return JsonResponse({'user': user_serializer.data})


class ContactView:
    @staticmethod
    @api_view(['GET', 'DELETE', 'PUT'])
    def view_contact_by_contact_id(request: Request, user_id: int, contact_id: int) -> JsonResponse:
        if request.method == 'GET':
            return ContactView.get_contact(user_id, contact_id)
        if request.method == 'DELETE':
            return ContactView.delete_contact(user_id, contact_id)
        if request.method == 'PUT':
            return ContactView.update_contact(user_id, contact_id, request.data)

    @staticmethod
    @api_view(['GET', 'POST'])
    def view_contact(request: Request, user_id: int) -> JsonResponse:
        if request.method == 'GET':
            return ContactView.get_all_contacts(user_id)
        if request.method == 'POST':
            return ContactView.add_contact(user_id, request.data)

    @staticmethod
    def get_contact(user_id: int, contact_id: int) -> JsonResponse:
        contact = Contact.get_contact(user_id, contact_id)
        contact_serializer = ContactSerializer(contact)
        return JsonResponse({'contact': contact_serializer.data})

    @staticmethod
    def update_contact(user_id: int, contact_id: int, data: dict) -> JsonResponse:
        contact = Contact.update_contact(user_id, contact_id, data)
        contact_serializer = ContactSerializer(contact)
        return JsonResponse({'contact': contact_serializer.data})

    @staticmethod
    def delete_contact(user_id: int, contact_id: int) -> JsonResponse:
        contact = Contact.delete_contact(user_id, contact_id)
        contact_serializer = ContactSerializer(contact)
        return JsonResponse({'contact': contact_serializer.data})

    @staticmethod
    def get_all_contacts(user_id: int) -> JsonResponse:
        all_contacts = Contact.get_all_contacts(user_id)
        contact_serializer = ContactSerializer(all_contacts, many=True)
        return JsonResponse({'phonebook_contacts': contact_serializer.data})

    @staticmethod
    def add_contact(user_id: int, data: dict) -> JsonResponse:
        contact = Contact.add_contact(user_id, data)
        contact_serializer = ContactSerializer(contact)
        return JsonResponse({'contact': contact_serializer.data})