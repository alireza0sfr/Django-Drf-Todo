from django.db import models


class TaskStatus(models.IntegerChoices):
    DONE = 1, 'Done'
    PUBLISHED = 2, 'Published'
    ARCHIVED = 3, 'Archived'
    DELETED = 4, 'Deleted'


class TaskPriority(models.TextChoices):
    HIGH = 1, 'High'
    MEDIUM = 2, 'Medium'
    LOW = 3, 'Low'
