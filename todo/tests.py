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

import requests, json

Application = get_application_model()

class TaskModelTest(TestCase):
    """ 
    Testeando el modelo creado 
    """
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
        self.task = Task.objects.create(name='tarea', description='description tarea')

        self.application = Application(
            name="todo",
            user=self.user,
            client_type=Application.CLIENT_PUBLIC,
            authorization_grant_type=Application.GRANT_PASSWORD,
        )
        self.application.save()

        self.token_request_data = {
            'grant_type': 'password',
            'username': 'rulz',
            'password': '12345'
        }

        self.auth_headers = self.get_basic_auth_header(
            urllib.quote_plus(self.application.client_id),
            urllib.quote_plus(self.application.client_secret))

        self.response = self.client.post(reverse('oauth2_provider:token'), data=self.token_request_data, **self.auth_headers)
        content = json.loads(self.response.content.decode("utf-8"))
        self.headers = {'Authorization': 'Bearer %(token)s' % {'token': content['access_token']}}

    def test_list_task(self):
        response = self.client.get(reverse('tasks-list'), **self.headers)
        content = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['count'], 1)
        self.assertEqual(content['results'][0]['name'], self.task.name)
        self.assertEqual(content['results'][0]['description'], self.task.description)
        self.assertEqual(content['results'][0]['assigned_to'], self.task.assigned_to)
        self.assertFalse(content['results'][0]['done'])

    def test_list_task_two(self):
        task = Task.objects.create(name='tarea2', description='description tarea2', done=True)
        response = self.client.get(reverse('tasks-list'), **self.headers)
        content = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['count'], 2)
        self.assertEqual(content['results'][0]['name'], self.task.name)
        self.assertEqual(content['results'][0]['description'], self.task.description)
        self.assertEqual(content['results'][0]['assigned_to'], self.task.assigned_to)
        self.assertFalse(content['results'][0]['done'])
        self.assertEqual(content['results'][1]['name'], task.name)
        self.assertEqual(content['results'][1]['description'], task.description)
        self.assertEqual(content['results'][1]['assigned_to'], task.assigned_to)
        self.assertTrue(content['results'][1]['done'])

    def test_detail_task(self):
        response = self.client.get(reverse('tasks-detail', kwargs={'pk':1}), **self.headers)
        content = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['name'], self.task.name)
        self.assertEqual(content['description'], self.task.description)
        self.assertEqual(content['assigned_to'], self.task.assigned_to)
        self.assertFalse(content['done'])

    def test_update_task(self):
        data = {'name':'tarea update', 'description':'update', 'done':True}
        response = self.client.put(reverse('tasks-detail', kwargs={'pk':1}), data=json.dumps(data), 
            content_type='application/json',**self.headers)
        content = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['name'], data['name'])
        self.assertEqual(content['description'], data['description'])
        self.assertEqual(content['assigned_to'], self.task.assigned_to)
        self.assertTrue(content['done'])

    def test_create_task(self):
        data = {'name':'new tarea', 'description':'new descripcion'}
        response = self.client.post(reverse('tasks-list'), data=json.dumps(data), 
            content_type='application/json',**self.headers)
        content = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(content['name'], data['name'])
        self.assertEqual(content['description'], data['description'])
        self.assertEqual(content['assigned_to'], None)
        self.assertFalse(content['done'])


