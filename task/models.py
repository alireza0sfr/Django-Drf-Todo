from django.db import models

from common.models import BaseModel
from enums.base import TaskStatus
from todo_app_raw.settings import AUTH_USER_MODEL


class Task(BaseModel):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=TaskStatus.PUBLISHED)
    category = models.ForeignKey('Category', on_delete=models.SET_DEFAULT, default=None)

    def __str__(self):
        return self.title


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
