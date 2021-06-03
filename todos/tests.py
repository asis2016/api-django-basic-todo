import uuid
from django.test import TestCase
from .models import Todo

class TodoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """ "The creation of initial data at the class level." """
        Todo.objects.create(id='550e8400e29b41d4a716446655440000', title='first todo', body='a body here')
        

    def test_title_content(self):
        """ Test if title content works. """
        todo=Todo.objects.get(id='550e8400e29b41d4a716446655440000')
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'first todo')


    def test_body_content(self):
        """ Test if body content works. """
        todo=Todo.objects.get(id='550e8400e29b41d4a716446655440000')
        expected_object_name=f'{todo.body}'
        self.assertEquals(expected_object_name, 'a body here')