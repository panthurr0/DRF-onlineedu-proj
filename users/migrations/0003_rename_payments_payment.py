# Generated by Django 5.0.6 on 2024-06-12 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0003_alter_lesson_course"),
        ("users", "0002_payments"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Payments",
            new_name="Payment",
        ),
    ]
