from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import Base_model

class User(AbstractUser, Base_model):
    nick_name = models.CharField(max_length=150)

    class Meta:
        ordering = ("-created", )
        db_table = "users"

    def __str__(self):
        return self.username


