from django.urls import include, path

from api.router import router
from task.views import TaskModelViewSet, CategoryViewSet
from accounts.urls import urlpatterns as accounts_urlpatterns

router.register('tasks', TaskModelViewSet, basename='tasks')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
    path('accounts/', include(accounts_urlpatterns)),
]