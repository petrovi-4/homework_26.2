# Generated by Django 5.0.6 on 2024-07-08 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=100, verbose_name='цена'),
        ),
    ]
