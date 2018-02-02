from rest_framework import serializers

from project.api.models import Profile, Picture


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Picture
        fields = ('title',
                  'image',
                  'description',
                  'upload_date',
                  'last_modified',
                  'author')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'url', 'username', 'email', 'groups', 'birthday', 'bio')
