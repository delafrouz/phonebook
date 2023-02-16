from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.contrib.auth.hashers import make_password


class UserController:
    @staticmethod
    def get_user(user_id: int):
        return User.objects.get(id=user_id)

    @staticmethod
    def add_user(data: dict) -> User:
        hashed_password = make_password(data.get('password', '{}_password'.format(data.get('username'))))
        data = {**data, 'password': hashed_password}
        user = User.objects.create(**data, is_superuser=True)
        return user

    @staticmethod
    def update_user(user_id: int, data: dict) -> User:
        User.objects.filter(id=user_id).update(**data)
        return User.objects.get(id=user_id)

    @staticmethod
    def delete_user(user_id: int) -> User:
        user = User.objects.get(id=user_id)
        user.delete()
        return user

    @staticmethod
    def get_all_users() -> QuerySet:
        return User.objects.all()
