from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создание пользователя суперпользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@gmail.com',
            first_name='Admin',
            last_name='Adminov',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('123456')
        user.save()
