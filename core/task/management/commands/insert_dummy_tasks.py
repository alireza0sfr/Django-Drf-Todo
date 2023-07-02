from django.core.management.base import BaseCommand

from task.models import Task
from tests.task.factories import TaskFactory

class Command(BaseCommand):
    help = "Inserts 5 dummy tasks."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        for _ in range(5):
            TaskFactory()