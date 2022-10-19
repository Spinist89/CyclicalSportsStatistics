from django.contrib import admin

from .models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "created_at",
    )


admin.site.register(Group, GroupAdmin)
