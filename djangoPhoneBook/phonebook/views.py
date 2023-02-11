from django.http import HttpResponse
from django.http.request import HttpRequest


class PhonebookView:
    @staticmethod
    def view_all_phonebook(request: HttpRequest):
        # TODO get all profiles
        return HttpResponse('this is the whole phonebook')

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