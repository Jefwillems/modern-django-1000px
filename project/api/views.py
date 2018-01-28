from django.contrib.auth.models import User
from rest_framework import viewsets
from project.api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().select_related('profile')
    serializer_class = UserSerializer
