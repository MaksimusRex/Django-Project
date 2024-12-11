from django import forms
from django.db import models

from theProject2.criminals.models import CriminalMainInfo, CriminalDetailInfo
from theProject2.prisons.models import Prison


class CriminalCreationForm(forms.ModelForm):
    class Meta:
        model = CriminalMainInfo
        exclude = ['is_approved', 'policeman', 'prison']

class CriminalDetailInfoForm(forms.ModelForm):
    class Meta:
        model = CriminalDetailInfo
        exclude = ['main_info']
        widgets = {
            'address': forms.Textarea(attrs={
                'style': 'resize: none;',
                'rows': 4,
                'cols': 50,
            }),
            'description': forms.Textarea(attrs={
                'style': 'resize: none;',
                'rows': 4,
                'cols': 50,
            })
        }

class CriminalEditMainInfoForm(forms.ModelForm):
    class Meta:
        model = CriminalMainInfo
        exclude = ['is_approved', 'policeman']

    def __init__(self, *args, **kwargs):
        # Extract the instance (criminal) from kwargs if present
        criminal_instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)

        if criminal_instance:
            # Calculate total criminal points
            criminal_points = criminal_instance.total_crime_points()

            # Filter prisons based on security level and required points
            self.fields['prison'].queryset = Prison.objects.all()
            if criminal_points < 3:
                self.fields['prison'].queryset = Prison.objects.none()
            elif 3 < criminal_points < 7:
                self.fields['prison'].queryset = Prison.objects.filter(security_level="Low")
            elif 7 < criminal_points < 15:
                self.fields['prison'].queryset = Prison.objects.filter(security_level="Mid")
            elif 15 < criminal_points:
                self.fields['prison'].queryset = Prison.objects.filter(security_level="High")

        else:
            # Default to show no prisons if the instance is not provided
            self.fields['prison'].queryset = Prison.objects.none()
