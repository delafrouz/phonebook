from django.urls import path

from . import views

urlpatterns = [
    path('', views.PhonebookView.view_all_phonebook, name='complete_phonebook'),
    path('<int:user_id>/', views.PhonebookView.view_user_phonebook, name='user_phonebook'),
    path('user/<int:user_id>/', views.UserView.view_profile_by_id, name='user_profile'),
    path('user/', views.UserView.view_profile, name='user_profile')
    # path('', views.index, name='index'),
]
