from django.urls import path
from .views import Login, RegistrationView

urlpatterns=[
    path('login/' ,  Login.as_view()),
    path('register/', RegistrationView.as_view()),
]