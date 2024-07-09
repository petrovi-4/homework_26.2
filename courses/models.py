from django.conf import settings
from django.db import models

from config.settings import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview_image = models.ImageField(
        upload_to='course_images/',
        verbose_name='Изображение',
        **NULLABLE
    )
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)
    price = models.IntegerField(verbose_name='цена', default=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview_image = models.ImageField(
        upload_to='course_images/',
        verbose_name='Изображение',
        **NULLABLE
    )
    description = models.TextField(verbose_name='описание')
    link_to_video = models.URLField(verbose_name='ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, related_name='subscriptions')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, related_name='subscriptions')
    is_activ = models.BooleanField(verbose_name='подписан')

    def __str__(self):
        return f'{self.pk}: user - {self.user} course - {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
