from django.db import models


class TaskStatus(models.IntegerChoices):
    PUBLISHED = 1, 'Published'
    ARCHIVED = 2, 'Archived'
    DELETED = 3, 'Deleted'


class TaskPriority(models.TextChoices):
    HIGH = 1, 'High'
    MEDIUM = 2, 'Medium'
    LOW = 3, 'Low'
