from django.urls.conf import path
from .views import TodoListAPIView, TodoRetrieveAPIView, UserDetail, UserList

urlpatterns = [

    path('users/<int:pk>/', UserDetail.as_view()),
    path('users/', UserList.as_view()),

    path('<uuid:pk>/', TodoRetrieveAPIView.as_view()),
    path('', TodoListAPIView.as_view()),
]