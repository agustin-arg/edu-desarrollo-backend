from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .models import User
from converter.models import File
from converter.serializers import FileSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
import rest_framework.status as status


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"

    @action(detail=True, methods=["get"])
    def files(self, request, id=None):
        """List files for a user. Returns serialized file data or 404 if user not found."""
        user = get_object_or_404(User, id=id)
        files_qs = File.objects.filter(user=user)
        serializer = FileSerializer(files_qs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
