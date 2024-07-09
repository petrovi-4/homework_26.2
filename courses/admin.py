from django.contrib import admin

from courses.models import Lesson, Course, Subscription
from users.models import Payment


@admin.register(Lesson)
class LeesonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'course', 'owner')
    search_fields = ('title', 'course', 'owner')


@admin.register(Course)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'owner')
    search_fields = ('title', 'owner')


@admin.register(Subscription)
class SubscribtionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'course', 'is_activ')


@admin.register(Payment)
class PaymetAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'course', 'date', 'amount')