from django.urls import path

from . import views

urlpatterns = [
    path('', views.PhonebookView.view_all_phonebook, name='complete_phonebook'),
    path('<int:user_id>/', views.PhonebookView.view_user_phonebook, name='user_phonebook'),
    path('user/<int:user_id>/', views.UserView.view_profile_by_id, name='user_profile_by_id'),
    path('user/', views.UserView.view_profile, name='user_profile'),
    path('contact/<int:user_id>/<int:contact_id>/', views.ContactView.view_contact_by_contact_id, name=''),
    path('contact/<int:user_id>/', views.ContactView.view_contact, name=''),
]
