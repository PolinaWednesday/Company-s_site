from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User
from users.permissions import IsModerator, IsSuperUser, IsUserOwner
from users.serializers import UserSerializer, UserCreateSerializer


class UserCreateAPIView(CreateAPIView):
    """Класс для создания пользователя"""
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserUpdateAPIView(UpdateAPIView):
    """Класс для обновления пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUserOwner | IsModerator | IsSuperUser]


class UserListAPIView(ListAPIView):
    """Класс для получения списка пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsSuperUser]

    def get_object(self):
        return self.request.user


class UserRetrieveAPIView(RetrieveAPIView):
    """Класс для получения пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUserOwner | IsModerator | IsSuperUser]


class UserDeleteAPIView(DestroyAPIView):
    """Класс для удаления пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUserOwner | IsSuperUser]
