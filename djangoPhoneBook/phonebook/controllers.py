from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.contrib.auth.hashers import make_password

from djangoPhoneBook.phonebook.models import Contact, Tag


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


class ContactController:
    @staticmethod
    def get_contact(user_id: int, contact_id: int) -> 'Contact':
        contact = Contact.objects.get(user_id=user_id, id=contact_id)
        return contact

    @staticmethod
    def update_contact(user_id: int, contact_id: int, data: dict) -> 'Contact':
        contact = Contact.objects.get(user_id=user_id, id=contact_id)
        for key in data:
            setattr(contact, key, data[key])
        contact.save()
        return contact

    @staticmethod
    def delete_contact(user_id: int, contact_id: int) -> 'Contact':
        contact = Contact.objects.get(user_id=user_id, id=contact_id)
        contact.delete()
        return contact

    @staticmethod
    def get_all_contacts(user_id: int) -> ['Contact']:
        return Contact.objects.filter(user_id=user_id)

    @staticmethod
    def add_contact(user_id: int, data: dict) -> 'Contact':
        # TODO is this correct? should I pass the user object or user_id is enough?
        contact = Contact.objects.create(**data, user_id=user_id)
        return contact


class TagController:
    @staticmethod
    def get_tags_of_user(user_id: int) -> ['Tag']:
        tags = Tag.objects.filter(user_id=user_id)
        return tags

    @staticmethod
    def get_tagged_contacts(user_id: int, tag_name: str) -> [Contact]:
        contacts = Contact.objects.filter(tag__user_id=user_id, tag__name__contains=tag_name)
        return contacts

    @staticmethod
    def get_contacts_and_tags(user_id: int) -> [(Contact, ['Tag'])]:
        contacts = Contact.objects.filter(user_id=user_id)
        contacts_and_tags_list = []
        for contact in contacts:
            tags = Tag.objects.filter(contact__in=[contact.id])
            contacts_and_tags_list.append((contact, tags))
        return contacts_and_tags_list

    @staticmethod
    def tag_contact(user_id: int, contact_id: int, tag_name: str) -> (Contact, 'Tag'):
        user = User.objects.get(id=user_id)
        tag_name = tag_name or '{}\'s new tag'.format(user.first_name)
        tag = Tag.objects.get_or_create(name=tag_name, user_id=user_id)[0]
        tag.contact.add(contact_id)
        return Contact.objects.get(id=contact_id), tag
