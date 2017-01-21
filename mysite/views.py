from django.contrib.auth.models import User
from rest_framework import viewsets,permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer