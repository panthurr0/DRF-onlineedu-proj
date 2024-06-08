from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)
    phone_number = models.CharField(verbose_name='номер телефона', max_length=30, **NULLABLE)
    avatar = models.ImageField(verbose_name='аватар', upload_to='users/', **NULLABLE)
    city = models.CharField(verbose_name='город', max_length=100, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
