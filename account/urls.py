from django.urls import path
from .views import LoginView, RegistrationView


urlpatterns = [
    path('', LoginView.as_view(), name='account'),
    path('register/', RegistrationView.as_view(), name="register")
] 