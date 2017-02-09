import django.contrib.auth.models
import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = django.contrib.auth.models.User
        fields = ('url', 'username', 'email', 'groups')


class StatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Statistics
        fields = ('new_order', 'new_visitors', 'new_user', 'profit_today')