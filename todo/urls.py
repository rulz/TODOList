from django.conf.urls import url, patterns, include

from .api import UserViewSet, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, base_name='users')
router.register('tasks', TaskViewSet, base_name='tasks')

urlpatterns = [
	url(r'^api/', include(router.urls)),
	url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]