from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_api.serializers import GroupSerializer, EmailSerializer, DispatchSerializer
from email_dispatch.models import Email, Group, Dispatch
  

class EmailViewSet(viewsets.ModelViewSet):
  """API endpoint that allows users to be viewed or edited."""
  queryset = Email.objects.all()
  serializer_class = EmailSerializer
  

class GroupViewSet(viewsets.ModelViewSet):
  """API endpoint that allows groups to be viewed or edited."""
  queryset = Group.objects.all()
  serializer_class = GroupSerializer


class DispatchViewSet(viewsets.ModelViewSet):
  """API endpoint that allows users to be viewed or edited."""
  queryset = Dispatch.objects.all()
  serializer_class = DispatchSerializer