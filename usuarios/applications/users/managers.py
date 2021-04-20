from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager,models.Manager):

    #def create_user(self):
    
    def create_superuser(self,username,password=None,**extra_fields):
        return self._create_user
