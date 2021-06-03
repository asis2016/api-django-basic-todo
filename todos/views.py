from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions

from .models import Todo
from .permissions import IsAuthorOrReadOnly
from .serializers import TodoSerializer, UserSerializer


class TodoViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """ Viewset for todo. """
    permission_classes = (IsAuthorOrReadOnly, permissions.IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class=UserSerializer