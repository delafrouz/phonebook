from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    #TODO change to email field
    email = models.CharField(max_length=80, null=True)
    address = models.CharField(max_length=80, null=True)
    secondary_phone_number = models.CharField(max_length=80, null=True)
    job = models.CharField(max_length=20, null=True)
    middle_name = models.CharField(max_length=80, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}: {} <{}>'.format(self.first_name, self.last_name, self.phone_number, self.email)

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


class Tag(models.Model):
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.ManyToManyField(Contact)

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
