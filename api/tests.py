from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Message

class ModelTestCase(TestCase):
    """This class defines the test suite for the messages model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.message_text = "Hello Greystone!"
        self.message = Message(message_text=self.message_text)

    def test_model_can_create_a_message(self):
        """Test the Message model can create a message."""
        old_count = Message.objects.count()
        self.message.save()
        new_count = Message.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.message_data = {'message_text': 'Hey Robert!', 'id': 1}
        self.response = self.client.post(
            reverse('create'),
            self.message_data,
            format="json")

    def test_api_can_create_a_message(self):
        """Test the api can create a message creation."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    
    def test_api_can_get_a_message(self):
        """Test the api can get a given message."""
        message = Message.objects.get()
        print message
        response = self.client.get(
            '/message/',
            kwargs={'pk': message.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, message)

    def test_api_can_update_message(self):
        """Test the api can update a given message."""
        message = Message.objects.get()
        change_message = {'message_text': 'Something different'}
        res = self.client.put(
            reverse('details', kwargs={'pk': message.id}),
            change_message, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_message(self):
        """Test the api can delete a message."""
        message = Message.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': message.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        