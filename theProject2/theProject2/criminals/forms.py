from django import forms

from theProject2.criminals.models import CriminalMainInfo, CriminalDetailInfo


class CriminalCreationForm(forms.ModelForm):
    class Meta:
        model = CriminalMainInfo
        exclude = ['is_approved', 'policeman']

class CriminalDetailInfoForm(forms.ModelForm):
    class Meta:
        model = CriminalDetailInfo
        exclude = ['main_info']
