from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """ Создание модератора """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='moderator@gmail.com',
            first_name='Moderator',
            last_name='Moderatorov',
            is_superuser=False,
            is_staff=True,
            is_active=True
        )

        user.set_password('12345678')
        user.save()
