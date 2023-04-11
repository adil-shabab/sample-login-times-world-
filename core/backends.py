from django.contrib.auth.backends import BaseBackend
from .models import *

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CustomUsers.objects.get(email=email)
            if user.check_password(password):
                return user
        except CustomUsers.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUsers.objects.get(pk=user_id)
        except CustomUsers.DoesNotExist:
            return None
