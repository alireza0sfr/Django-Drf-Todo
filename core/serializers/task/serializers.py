from rest_framework.serializers import ModelSerializer, ReadOnlyField

from task.models import Task, Category
from accounts.models import Profile


class TaskModelSerializer(ModelSerializer):
    snippet = ReadOnlyField(source='get_snippet')

    class Meta:
        model = Task
        fields = ['id', 'author', 'title', 'content', 'snippet', 'status', 'category', 'priority', 'created_date']
        read_only_fields = ['author']

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id=self.context.get('request').user.id)
        return super().create(validated_data)


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_date']
