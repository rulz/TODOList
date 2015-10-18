from django.test import TestCase
from django.contrib.auth.models import User

from .models import Task

class TaskTest(TestCase):

    def setUp(self):
        user = User.objects.create_user('rulz', 'raulsetron@gmail.com', '12345')
        task = Task.object.create()

