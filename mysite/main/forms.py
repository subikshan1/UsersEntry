"""modules"""
from django import forms

from .models import Users

"""Registration"""


class Registration(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['FirstName', 'LastName', 'DOB', 'Gender', 'National', 'City', 'Pin', 'State', 'Qualification',
                  'Salary', 'PanNum']
