# Generated by Django 5.0.6 on 2024-06-12 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_rename_course_description_lesson_lesson_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="lesson",
                to="materials.course",
                verbose_name="Курс",
            ),
        ),
    ]
