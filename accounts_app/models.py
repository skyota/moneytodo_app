from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  first_name = None
  last_name = None
  last_login = None
  is_superuser = None
  is_staff = None
  # updated_at = models.DateTimeField(auto_now=True)