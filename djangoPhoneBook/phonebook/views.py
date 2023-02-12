from django.http import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from .models import User, Contact, Connection
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
        if request.method == 'DELETE':
            return UserView.delete_user(user_id)
        if request.method == 'PUT':
            return UserView.update_user(user_id, request.data)

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
    def add_user(data: dict) -> JsonResponse:
        user = User.add_user(data)
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


class ContactView:
    @staticmethod
    def view_profile(request: HttpRequest):
        # TODO handle all CRUD operations for User
        pass

    @staticmethod
    def get_user(request: HttpRequest):
        # TODO get user by id
        pass

    @staticmethod
    def add_user(request: HttpRequest):
        # TODO add new user
        pass

    @staticmethod
    def update_user(request: HttpRequest):
        # TODO update user
        pass

    @staticmethod
    def delete_user(request: HttpRequest):
        # TODO delete user
        pass