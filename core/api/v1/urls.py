from api.router import router
from task.views import TaskModelViewSet, CategoryViewSet

router.register('tasks', TaskModelViewSet, basename='tasks')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = router.urls
