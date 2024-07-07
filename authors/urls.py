from django.urls import path

from authors.views import register_view

urlpatterns = [
    path('register/', register_view, name='register')
]
