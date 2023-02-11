from django.http import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from .models import User, Contact, Connection
from .serializers import UserSerializer, ContactSerializer
from rest_framework.decorators import api_view


class PhonebookView:
    @staticmethod
    @api_view(['GET'])
    def view_all_phonebook(request: HttpRequest):
        all_users = User.get_all_users()
        user_serializer = UserSerializer(all_users, many=True)
        return JsonResponse({'phonebook_users': user_serializer.data})

    @staticmethod
    def view_user_phonebook(request: HttpRequest, user_id: int):
        # TODO get one users contacts
        return HttpResponse('this is one persons phonebook at id={}'.format(user_id))


class UserView:
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