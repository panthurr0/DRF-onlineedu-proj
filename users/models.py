from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="почта", unique=True)
    phone_number = models.CharField(
        verbose_name="номер телефона", max_length=30, **NULLABLE
    )
    avatar = models.ImageField(verbose_name="аватар", upload_to="users/", **NULLABLE)
    city = models.CharField(verbose_name="город", max_length=100, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    TRANSFER = "Перевод"
    CASH = "Наличные"

    PAYMENT_METHODS = [
        (TRANSFER, "Перевод на счёт"),
        (CASH, "Наличными"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    pay_date = models.DateField(verbose_name="Дата оплаты", **NULLABLE)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE)

    pay_sum = models.PositiveIntegerField(verbose_name="Сумма оплаты")

    pay_method = models.CharField(
        verbose_name="Способ оплаты", choices=PAYMENT_METHODS, default=TRANSFER
    )

    url = models.CharField(verbose_name="Ссылка на оплату", **NULLABLE)

    session_id = models.CharField(verbose_name="ID сессии", **NULLABLE)

    def __str__(self):
        return (
            f"{self.user}: {self.pay_method}."
            f"{self.course if self.course else self.lesson}"
        )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"


class Subscription(models.Model):
    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.SET_NULL, **NULLABLE
    )

    course = models.ForeignKey(
        Course, verbose_name="Курс", on_delete=models.SET_NULL, **NULLABLE
    )

    def __str__(self):
        return f"{self.user} имеет подписку на {self.course}"

    class Meta:
        verbose_name = "Подписка на курс"
        verbose_name_plural = "Подписки на курс"
