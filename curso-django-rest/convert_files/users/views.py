from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["GET", "POST"])
def list_users(request):
    if request.method == "GET":
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        user_serializer = UserSerializer(data = request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    

@api_view(["GET", "PUT", "DELETE"])
def detail_user(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)
    if request.method == 'PUT':
        user_serializer = UserSerializer(user, data = request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)