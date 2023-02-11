from django.urls import path

from . import views

urlpatterns = [
    path('', views.PhonebookView.view_all_phonebook, name='complete_phonebook'),
    path('<int:user_id>/', views.PhonebookView.view_user_phonebook, name='user_phonebook'),
    # path('', views.index, name='index'),
]
