from django.urls import path

from . import views

urlpatterns = [
    path('', views.PhonebookView.view_all_phonebook, name='complete_phonebook'),
    path('<int:user_id>/', views.PhonebookView.view_user_phonebook, name='user_phonebook'),
    path('user/<int:user_id>/', views.UserView.view_profile_by_id, name='user_profile_by_id'),
    path('user/', views.UserView.view_profile, name='user_profile'),
    path('contact/<int:user_id>/<int:contact_id>/', views.ContactView.view_contact_by_contact_id, name='contact_view'),
    path('contact/<int:user_id>/', views.ContactView.view_contact, name='user_contacts_view'),
    path('tag/<int:user_id>/', views.TagView.get_tags_of_user, name='user_tags_view'),
    path('tag/<int:user_id>/<str:tag_name>/', views.TagView.get_tagged_contacts, name='get_tagged_contacts'),
    path('tag/contact/<int:user_id>/', views.TagView.tag_contact_view, name='tag_contact_view'),
]
