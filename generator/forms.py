from django import forms

from .models import Profile

class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['email']