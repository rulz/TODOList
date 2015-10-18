from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from oauth2_provider.models import get_application_model, AccessToken
from oauth2_provider.tests.test_utils import TestCaseUtils

from .models import Task

from datetime import datetime

try:
    import urllib.parse as urllib
except ImportError:
    import urllib

import requests

Application = get_application_model()

class TaskModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('rulz', 'raulsetron@gmail.com', '12345')
        self.user2 = User.objects.create_user('rulz2', 'rulz0001@gmail.com', '12345')
        self.task = Task.objects.create(name='tarea', description='description tarea')
        #assigned_to, name, description, done, created, modified 

    def test_create(self):
        task = Task.objects.create(name='tarea', description='description tarea')
        self.assertEquals(task.name, 'tarea')
        self.assertEquals(task.description, 'description tarea')
        self.assertEquals(task.assigned_to, None)
        self.assertEquals(type(task.name), str)
        self.assertEquals(task.created.date(), datetime.now().date())
        self.assertFalse(task.done)
        self.assertNotEquals(task.created, task.modified)

    def test_assigned_to_task(self):
        self.task.assigned_to = self.user
        self.assertEquals(self.task.name, 'tarea')
        self.assertEquals(self.task.description, 'description tarea')
        self.assertEquals(self.task.assigned_to, self.user)
        self.assertFalse(self.task.done)

    def test_change_done(self):
        self.task.assigned_to = self.user
        self.task.done = True
        self.assertEquals(self.task.name, 'tarea')
        self.assertEquals(self.task.description, 'description tarea')
        self.assertEquals(self.task.assigned_to, self.user)
        self.assertTrue(self.task.done)
        self.assertEquals(type(self.task.done), bool)

class TaskApiTest(TestCaseUtils, TestCase):

    def setUp(self):
        self.user = User.objects.create_user('rulz', 'raulsetron@gmail.com', '12345')
        self.application = Application(
            name="todo",
            user=self.user,
            client_type=Application.CLIENT_PUBLIC,
            authorization_grant_type=Application.GRANT_CLIENT_CREDENTIALS,
        )
        self.application.save()

        token_request_data = {
            'grant_type': 'password',
            'username': 'rulz',
            'password': '12345'
        }

        auth_headers = self.get_basic_auth_header(
            urllib.quote_plus(self.application.client_id),
            urllib.quote_plus(self.application.client_secret))
        
        self.response = self.client.post(reverse('oauth2_provider:token'), data=token_request_data, **auth_headers)

    def test_token(self):
        data = self.token_request_data
        r = requests.post('http://localhost:8000/o/token/', 
            data=data)
        print r.json()
        self.assertEqual(self.response.status_code, 200)

