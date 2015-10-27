from django.conf.urls import url#, patterns, include
from . import views

# from .api import UserViewSet, TaskViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('users', UserViewSet, base_name='users')
# router.register('tasks', TaskViewSet, base_name='tasks')

# urlpatterns = [
#   url(r'^api/', include(router.urls)),
#   url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
# ]

urlpatterns = [
    url(r'^tareas/$', views.task_list, name='task_list'),
    url(r'^crear/tarea/$', views.task_create, name='task_create'),
    url(r'^editar/tarea/(?P<pk>\d+)/$', views.task_update, name='task_update'),
    url(r'^detalle/tarea/(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    url(r'^eliminar/tarea/(?P<pk>\d+)/$', views.task_delete, name='task_delete'),
]