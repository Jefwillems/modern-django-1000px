from rest_framework import viewsets
from project.api.models import Picture, Profile
from project.api.serializers import PictureSerializer, ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PictureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pictures to be viewed or edited
    """
    queryset = Picture.objects.all().select_related('author')
    serializer_class = PictureSerializer
