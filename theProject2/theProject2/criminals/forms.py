from django import forms

from theProject2.criminals.models import CriminalMainInfo, CriminalDetailInfo
from theProject2.prisons.models import Prison


class CriminalCreationForm(forms.ModelForm):
    prison = forms.ModelChoiceField(
        queryset=Prison.objects.none(),  # Default to empty queryset
        required=False,
        help_text="Assign a prison to the criminal.",
        widget=forms.Select
    )

    class Meta:
        model = CriminalMainInfo
        exclude = ['is_approved', 'policeman']

    def __init__(self, *args, **kwargs):
        # Pass criminal points as a keyword argument
        criminal_points = kwargs.pop('criminal_points', None)
        super().__init__(*args, **kwargs)

        if criminal_points is not None:
            # Filter prisons based on the criminal's points
            self.fields['prison'].queryset = Prison.objects.filter(required_points__lte=criminal_points)
        else:
            # Default to show no prisons if points are not provided
            self.fields['prison'].queryset = Prison.objects.none()

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
