from django.contrib.auth import get_user_model
from django.db.models import query
from rest_framework import generics, permissions

from .models import Todo
from .permissions import IsAuthorOrReadOnly
from .serializers import TodoSerializer, UserSerializer


class TodoListAPIView(generics.ListCreateAPIView):
    """ Listing all todo. """
    # permission_classes=(permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieving detail of a todo. """
    #permission_classes = (IsAuthorOrReadOnly,)
    #permission_classes=(permissions.IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# class TodoListAPIView(generics.ListAPIView):
# queryset=Todo.objects.all()
# serializer_class=TodoSerializer


# class TodoRetrieveAPIView(generics.RetrieveAPIView):
# queryset = Todo.objects.all()
# serializer_class = TodoSerializer

class UserList(generics.ListAPIView):
    """ List all users. """
    queryset = get_user_model().objects.all()
    serializer_class=UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """ Retrieve 1 user. """
    queryset = get_user_model().objects.all()
    serializer_class=UserSerializer