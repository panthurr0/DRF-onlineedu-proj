# Generated by Django 5.0.6 on 2024-06-26 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_rename_subscribe_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='session_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='ID сессии'),
        ),
        migrations.AddField(
            model_name='payment',
            name='url',
            field=models.CharField(blank=True, null=True, verbose_name='Ссылка на оплату'),
        ),
    ]
