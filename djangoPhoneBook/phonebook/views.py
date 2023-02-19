from django.http import JsonResponse

from .controllers import UserController, ContactController, TagController
from .serializers import UserSerializer, ContactSerializer, TagSerializer
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import permissions


class PhonebookView(APIView):
    def get(self, request: Request):
        all_users = UserController.get_all_users()
        user_serializer = UserSerializer(all_users, many=True)
        return JsonResponse({'phonebook_users': user_serializer.data})


class UserDetailView(APIView):
    def get(self, request: Request, user_id: int) -> JsonResponse:
        user = UserController.get_user(user_id)
        user_serializer = UserSerializer(user)
        return JsonResponse({'user': user_serializer.data})

    def put(self, request: Request, user_id: int) -> JsonResponse:
        user = UserController.update_user(self.request.user, request.data)
        user_serializer = UserSerializer(user)
        return JsonResponse({'user': user_serializer.data})

    def delete(self, request: Request, user_id: int) -> JsonResponse:
        user = UserController.delete_user(self.request.user)
        user_serializer = UserSerializer(user)
        return JsonResponse({'user': user_serializer.data})


class UserView(APIView):
    def post(self, request: Request) -> JsonResponse:
        user = UserController.add_user(request.data)
        user_serializer = UserSerializer(user)
        return JsonResponse({'user': user_serializer.data})


class ContactDetailView(APIView):
    def get(self, request: Request, user_id: int, contact_id: int) -> JsonResponse:
        contact = ContactController.get_contact(user_id, contact_id)
        contact_serializer = ContactSerializer(contact)
        return JsonResponse({'contact': contact_serializer.data})

    def put(self, request: Request, user_id: int, contact_id: int) -> JsonResponse:
        contact = ContactController.update_contact(self.request.user, contact_id, request.data)
        contact_serializer = ContactSerializer(contact)
        return JsonResponse({'contact': contact_serializer.data})

    def delete(self, request: Request, user_id: int, contact_id: int) -> JsonResponse:
        contact = ContactController.delete_contact(self.request.user, contact_id)
        contact_serializer = ContactSerializer(contact)
        return JsonResponse({'contact': contact_serializer.data})


class ContactView(APIView):
    def get(self, request: Request, user_id: int) -> JsonResponse:
        all_contacts = ContactController.get_all_contacts(user_id)
        contact_serializer = ContactSerializer(all_contacts, many=True)
        return JsonResponse({'phonebook_contacts': contact_serializer.data})

    def post(self, request: Request, user_id: int) -> JsonResponse:
        contact = ContactController.add_contact(self.request.user, request.data)
        contact_serializer = ContactSerializer(contact)
        return JsonResponse({'contact': contact_serializer.data})


class TagView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: Request, user_id: int) -> JsonResponse:
        tags = TagController.get_tags_of_user(user_id)
        tag_serializer = TagSerializer(tags, many=True)
        user_serializer = UserSerializer(UserController.get_user(user_id=user_id))
        return JsonResponse({'user': user_serializer.data, 'tags': tag_serializer.data})

    def post(self, request: Request, user_id: int) -> JsonResponse:
        contact_id = request.data.get('contact_id')
        tag_name = request.data.get('tag_name', '')
        contact, tag = TagController.tag_contact(self.request.user, contact_id, tag_name)
        tag_serializer = TagSerializer(tag)
        contact_serializer = ContactSerializer(contact)
        return JsonResponse({'contact': contact_serializer.data, 'tag': tag_serializer.data})


class TagDetailView(APIView):
    def get(self, request: Request, user_id: int, tag_name: str) -> JsonResponse:
        contacts = TagController.get_tagged_contacts(user_id, tag_name)
        contact_serializer = ContactSerializer(contacts, many=True)
        user_serializer = UserSerializer(UserController.get_user(user_id=user_id))
        return JsonResponse({'user': user_serializer.data, 'tag': tag_name, 'contacts': contact_serializer.data})


class TagAndContactView(APIView):
    def get(self, request: Request, user_id: int) -> JsonResponse:
        contacts_and_tags = TagController.get_contacts_and_tags(user_id)
        user_serializer = UserSerializer(UserController.get_user(user_id=user_id))
        response = []
        for contact_and_tags in contacts_and_tags:
            contact_serializer = ContactSerializer(contact_and_tags[0])
            tags_serializer = TagSerializer(contact_and_tags[1], many=True)
            response.append({'contact': contact_serializer.data, 'tags': tags_serializer.data})
        return JsonResponse({'user': user_serializer.data, 'contacts_and_tags': response})
