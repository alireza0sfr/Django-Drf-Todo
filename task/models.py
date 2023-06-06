from django.db import models

from common.models import BaseModel
from enums.task import TaskStatus, TaskPriority


class Task(BaseModel):
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    status = models.IntegerField(default=TaskStatus.PUBLISHED, choices=TaskStatus.choices)
    category = models.ForeignKey('Category', on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)
    priority = models.CharField(default=TaskPriority.LOW, choices=TaskPriority.choices, max_length=10)

    def __str__(self):
        return self.title


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
