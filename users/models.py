from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.settings import NULLABLE
from courses.models import Course, Lesson


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(
        upload_to='users/avatars/',
        verbose_name='Аватар',
        **NULLABLE
    )
    phone = models.CharField(max_length=40, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=35, verbose_name='Город', **NULLABLE)

    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name='Роль')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payment(models.Model):
    cash = 'Наличные'
    card = 'Банковская карта'
    payment_methods = [
        (cash, 'Наличные'),
        (card, 'Банковская карта'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment')
    date = models.DateField(verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, **NULLABLE, related_name='payment')
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, **NULLABLE, related_name='payment')
    amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    method = models.CharField(max_length=150, default=card, choices=payment_methods, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.pk} {self.date}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
