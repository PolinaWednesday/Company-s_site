from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from company.models import Contacts
from company.paginators import CompanyPagination
from company.serializers.contacts import ContactsSerializers
from users.permissions import IsOwner, IsModerator, IsSuperUser


class ContactsViewSet(ModelViewSet):
    """ Представление для работы с контактами """
    serializer_class = ContactsSerializers
    queryset = Contacts.objects.all()
    pagination_class = CompanyPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']

    def perform_create(self, serializer):
        new_obj = serializer.save()
        new_obj.creation_owner = self.request.user
        new_obj.save()

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [IsAuthenticated, IsOwner | IsModerator | IsSuperUser]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner | IsSuperUser]
        return [permission() for permission in self.permission_classes]
