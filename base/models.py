from django.db import models
from datetime import datetime


class Base_model(models.Model):
    is_deleted = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self, using=None, Keep_parents=False):
        self.is_deleted = True
        self.deleted = datetime.now()
        self.save()