from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "first_name",
        "last_name",
        "username",
        "email",
        "user_type",
        "is_superuser",
        "date_joined",
        "is_active",

    )


admin.site.register(User, UserAdmin)