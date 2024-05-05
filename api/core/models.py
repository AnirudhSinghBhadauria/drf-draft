import uuid

from django.db import models
from django.contrib.auth.base_user import BaseUserManager 
from django.contrib.auth.models import AbstractUser

ROLE = (
     ('ASSOCIATE_TRAINEE', "Associate trainee"),
     ('TECHNICAL_TRAINER', "Technical trainer"),
     ('MANAGER', "Manager"),
)

STATUS = (
     ('APPROVED', "Approved"),
     ('PENDING', "Pending"),
     ('REJECTED', "Rejected"),
)

class CustomUserManager(BaseUserManager):
     def create_user(
          self, email, password, **extra_fields
     ):
          email = self.normalize_email(email)
          
          user = self.model(
               email = email,
               **extra_fields
          )

          user.set_password(password)
          user.save()

          return user
          
     def create_superuser(
          self, email, password, **extra_fields
     ):
          extra_fields.setdefault("is_staff", True)
          extra_fields.setdefault("is_superuser", True)

          if extra_fields.get("is_staff") is not True:
               raise ValueError("Superuser has to have this TURE")

          if extra_fields.get("is_superuser") is not True:
               raise ValueError("Superuser has to have this TURE")

          return self.create_user(
               email = email, password = password, **extra_fields
          )


class User(AbstractUser):
     id = models.UUIDField(
          primary_key=True,
          editable=False, 
          default=uuid.uuid4
     )
     email = models.EmailField(
          max_length=255, unique=True, null=False
     )
     first_name = models.CharField(
          max_length=255, 
          default=''
     )
     last_name = models.CharField(
          max_length=255, 
          default=''
     )
     role = models.CharField(
          max_length=40,
          choices=ROLE, 
          default='Associate trainee'
     )
     authorization = models.ForeignKey(
          "core.Authorization", 
          on_delete=models.CASCADE, 
          related_name="user_authorizatoin",
          null=True
     )
     created = models.DateTimeField(
          auto_now_add=True, 
          editable=True
     )
     updated = models.DateTimeField(
          auto_now=True, 
          editable=True
     )

     objects = CustomUserManager()
     EMAIL_FIELD = "email"
     USERNAME_FIELD = "email"
     REQUIRED_FIELDS = ["password"]

     def __str__(self):
          return self.email

class Authorization(models.Model):
     id = models.UUIDField(
          primary_key=True,
          editable=False, 
          default=uuid.uuid4
     )
     user_email = models.EmailField(
          max_length=255, unique=True,
          null=False, default=''
     )
     administrator = models.ForeignKey(
          'core.User', 
          on_delete=models.CASCADE,
          related_name="authorizer",
          blank=True,
          null=True
     )
     status = models.CharField(
          max_length=40, 
          choices=STATUS, 
          default='Pending'
     )
     status_update = models.DateTimeField(
          auto_now_add=True,
          editable=True
     )

     def __str__(self):
          return self.user_email

