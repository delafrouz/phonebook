from django.http import JsonResponse

from .controllers import UserController
from .models import Contact, Tag
from .serializers import UserSerializer, ContactSerializer, TagSerializer
from rest_framework.decorators import api_view
from rest_framework.request import Request


class PhonebookView:
    @staticmethod
    @api_view(['GET'])
    def view_all_phonebook(request: Request):
        all_users = UserController.get_all_users()
        user_serializer = UserSerializer(all_users, many=True)
        return JsonResponse({'phonebook_users': user_serializer.data})


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
        user = UserController.get_user(user_id)
        user_serializer = UserSerializer(user)
        return JsonResponse({'user': user_serializer.data})

    @staticmethod
    def update_user(user_id: int, data: dict) -> JsonResponse:
        user = UserController.update_user(user_id, data)
        user_serializer = UserSerializer(user)
        return JsonResponse({'user': user_serializer.data})

    @staticmethod
    def delete_user(user_id: int) -> JsonResponse:
        user = UserController.delete_user(user_id)
        user_serializer = UserSerializer(user)
        return JsonResponse({'user': user_serializer.data})

    @staticmethod
    def add_user(data: dict) -> JsonResponse:
        user = UserController.add_user(data)
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


class TagView:
    @staticmethod
    @api_view(['GET'])
    def get_tags_of_user(request: Request, user_id: int) -> JsonResponse:
        tags = Tag.get_tags_of_user(user_id)
        tag_serializer = TagSerializer(tags, many=True)
        user_serializer = UserSerializer(UserController.get_user(user_id=user_id))
        return JsonResponse({'user': user_serializer.data, 'tags': tag_serializer.data})

    @staticmethod
    @api_view(['GET'])
    def get_tagged_contacts(request: Request, user_id: int, tag_name: str) -> JsonResponse:
        contacts = Tag.get_tagged_contacts(user_id, tag_name)
        contact_serializer = ContactSerializer(contacts, many=True)
        user_serializer = UserSerializer(UserController.get_user(user_id=user_id))
        return JsonResponse({'user': user_serializer.data, 'tag': tag_name, 'contacts': contact_serializer.data})

    @staticmethod
    @api_view(['GET', 'POST'])
    def tag_contact_view(request: Request, user_id: int) -> JsonResponse:
        if request.method == 'GET':
            return TagView.get_contacts_and_tags(user_id)
        if request.method == 'POST':
            return TagView.tag_contact(request.data, user_id)

    @staticmethod
    def get_contacts_and_tags(user_id: int) -> JsonResponse:
        contacts_and_tags = Tag.get_contacts_and_tags(user_id)
        user_serializer = UserSerializer(UserController.get_user(user_id=user_id))
        response = []
        for contact_and_tags in contacts_and_tags:
            contact_serializer = ContactSerializer(contact_and_tags[0])
            tags_serializer = TagSerializer(contact_and_tags[1], many=True)
            response.append({'contact': contact_serializer.data, 'tags': tags_serializer.data})
        return JsonResponse({'user': user_serializer.data, 'contacts_and_tags': response})

    @staticmethod
    def tag_contact(data: dict, user_id: int) -> JsonResponse:
        contact_id = data.get('contact_id')
        tag_name = data.get('tag_name', '')
        contact, tag = Tag.tag_contact(user_id, contact_id, tag_name)
        tag_serializer = TagSerializer(tag)
        contact_serializer = ContactSerializer(contact)
        return JsonResponse({'contact': contact_serializer.data, 'tag': tag_serializer.data})
