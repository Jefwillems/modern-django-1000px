from django.contrib.auth.models import User
from rest_framework import serializers
from project.api.models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('birth_date',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'profile')
