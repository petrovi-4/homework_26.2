from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Команда для создания пользователя
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='user@mail.com',
            is_active=True
        )

        user.set_password('123456')
        user.save()
