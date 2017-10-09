"""This module defines the api app unittest  test suite"""

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Bucketlist

# Model Tests

class ModelTestCase(TestCase):
    """This class defines the test suite for the Bucketlist model."""

    def setUp(self):
        """Defines the test client and other test variables."""
        user = User.objects.create_user(username="nerd")
        self.bucketlist_name = "Write world class code"
        self.bucketlist = Bucketlist(name=self.bucketlist_name, owner=user)

    def test_model_can_create_a_bucketlist(self):
        """Testing that the bucketlist model can create a bucketlist."""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)

# View Tests

class ViewsTestCase(TestCase):
    """Test suite for API views."""

    def setUp(self):
        """Test clients and variables definition"""
        user = User.objects.create_user(username='nerd')

        # Initialize the client and force it to authenticate
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.bucketlist_data = {'name':'Go to Ibiza', 'owner': user.id}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json"
        )

    def test_api_can_create_bucketlist(self):
        """Testing whether the api has bucket creation capability"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Testing authorization"""
        new_client = APIClient()
        res = new_client.get('/bucketlists/', kwargs={'pk': 3}, format='json')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_a_bucketlist(self):
        """Test the api can get the given bucketlist"""
        bucketlist = Bucketlist.objects.get(id=1)
        response = self.client.get(
            '/bucketlists/',
            kwargs={'pk': bucketlist.id},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given bucketlist."""

        bucketlist = Bucketlist.objects.get()
        change_bucketlist = {'name': 'Something new'}
        response = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_can_delete_bucketlist(self):
        """Test the api's ability to delete a bucketlist"""
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format="json", follow=True
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
