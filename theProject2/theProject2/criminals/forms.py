from django import forms

from theProject2.criminals.models import CriminalMainInfo


class CriminalCreationForm(forms.ModelForm):
    class Meta:
        model = CriminalMainInfo
        exclude = ['is_approved', 'policeman']