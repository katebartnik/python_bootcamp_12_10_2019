from django import forms


# class MathForm(forms.Form):
#     a = forms.CharField()
#     b = forms.CharField()
#     ...
from maths.models import Math


class MathForm(forms.ModelForm):
    class Meta:
        model = Math
        fields = ['a', 'b', 'operation']