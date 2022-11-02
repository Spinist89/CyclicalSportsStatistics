from django import forms

from .models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = (
            "title",
            "sportsmen",
        )
        labels = {
            "title": "Название группы:",
            "sportsmen": "Юнный поддаван:",
        }


