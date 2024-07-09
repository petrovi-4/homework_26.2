# Generated by Django 5.0.6 on 2024-07-01 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_payment_amount_alter_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('member', 'member'), ('moderator', 'moderator')], default='member', max_length=10, verbose_name='Роль'),
        ),
    ]