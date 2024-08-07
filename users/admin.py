from django.contrib import admin

from users.models import Payment, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "email")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_filter = ("id", "user", "course", "lesson", "pay_method")
