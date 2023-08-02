from celery import shared_task

from task.models import Task
from enums.task import TaskStatus

@shared_task
def delete_done_tasks():
    Task.objects.filter(status=TaskStatus.DONE).delete()