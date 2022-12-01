from django import forms

from users.models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = (
            "title",
        )
        labels = {
            "title": "Название группы:",
        }