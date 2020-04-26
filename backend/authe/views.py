from rest_framework import viewsets, permissions
from rest_framework import mixins
from django.contrib.auth.models import User
from rest_framework.response import Response

from authe.serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.AllowAny, ]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super(UserViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
