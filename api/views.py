"""This module defines the api's views"""

from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import BucketlistSerializer
from .models import Bucketlist

# API Views

class CreateView(generics.ListCreateAPIView):
    """This class handles the GET and POST requests for our rest api"""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """save the post data when crearing the new bucketlist"""
        serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the GET, PUT, PATCH and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
