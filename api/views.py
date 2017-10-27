from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import generics

from .serializers import MessageSerializer
from .models import Message

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new message."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer