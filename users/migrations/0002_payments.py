# Generated by Django 5.0.6 on 2024-06-12 09:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_rename_course_description_lesson_lesson_description"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pay_date",
                    models.DateField(blank=True, null=True, verbose_name="Дата оплаты"),
                ),
                ("pay_sum", models.PositiveIntegerField(verbose_name="Сумма оплаты")),
                (
                    "pay_method",
                    models.CharField(
                        choices=[
                            ("Перевод", "Перевод на счёт"),
                            ("Наличные", "Наличными"),
                        ],
                        default="Перевод",
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.course",
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.lesson",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
