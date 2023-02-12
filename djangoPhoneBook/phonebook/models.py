from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    user_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @staticmethod
    def get_user(user_id: int):
        return User.objects.get(user_id=user_id)

    @staticmethod
    def add_user(data: dict) -> 'User':
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        user_id = data.get('user_id', 0)
        user = User(first_name, last_name, user_id)
        user.save()
        return user

    def add_contact(self):
        # TODO add the contact in the contact table, get its id and add it in the connection table
        pass

    @staticmethod
    def get_all_users() -> ['User']:
        return User.objects.all()


class Contact(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    id = models.IntegerField(primary_key=True)
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
