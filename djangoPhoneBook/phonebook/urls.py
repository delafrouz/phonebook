from django.urls import path

from . import views

urlpatterns = [
    path('', views.PhonebookView.as_view(), name='complete_phonebook'),
    path('user/<int:user_id>/', views.UserDetailView.as_view(), name='user_profile_by_id'),
    path('user/', views.UserView.as_view(), name='user_profile'),
    path('contact/<int:user_id>/<int:contact_id>/', views.ContactDetailView.as_view(), name='contact_view'),
    path('contact/<int:user_id>/', views.ContactView.as_view(), name='user_contacts_view'),
    path('tag/<int:user_id>/', views.TagView.as_view(), name='users_tags_view'),
    path('tag/<int:user_id>/<str:tag_name>/', views.TagDetailView.as_view(), name='get_tagged_contacts'),
    path('tag/contact/<int:user_id>/', views.TagAndContactView.as_view(), name='tag_and_contact_view'),
]
