from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @staticmethod
    def get_user(user_id: int):
        return User.objects.get(id=user_id)

    @staticmethod
    def add_user(data: dict) -> 'User':
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        user = User.objects.create(first_name=first_name, last_name=last_name)
        return user

    @staticmethod
    def update_user(user_id: int, data: dict) -> 'User':
        user = User.objects.get(id=user_id)
        first_name = data.get('first_name', user.first_name)
        last_name = data.get('last_name', user.last_name)
        User.objects.filter(id=user_id).update(first_name=first_name, last_name=last_name)
        return User.objects.get(id=user_id)

    @staticmethod
    def delete_user(user_id: int) -> 'User':
        user = User.objects.get(id=user_id)
        user.delete()
        return user

    @staticmethod
    def get_all_users() -> ['User']:
        return User.objects.all()


class Contact(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    secondary_phone_number = models.CharField(max_length=80)
    job = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=80, default='')

    def __str__(self):
        return '{} {}: {} <{}>'.format(self.first_name, self.last_name, self.phone_number, self.email)

    def add_contact(self, first_name: str, last_name: str, phone_number: str, email: str,
                    address: str = '', secondary_phone_number: str = '', job: str = '', middle_name: str = ''):
        # TODO add a contact in the table and return its id
        pass


class Connection(models.Model):
    user_id = models.IntegerField()
    contact_id = models.IntegerField()

    def add_connection(self, user_id: int, contact_id: int):
        # TODO add a new connection
        pass
