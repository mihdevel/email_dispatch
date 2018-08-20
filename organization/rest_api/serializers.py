from django.contrib.auth.models import User, Group
from rest_framework import serializers
from email_dispatch.models import Email, Group, Dispatch


class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ('id', 'name')


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Email
        fields = ('id', 'email', 'group_id')


class DispatchSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Dispatch
    fields = ('id', 'template_id', 'group_id', 'date', 'text')