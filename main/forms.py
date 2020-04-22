from django import forms
from .models import Url


class AddUrlForm(forms.ModelForm):

    class Meta():
        model = Url
        fields = ('title', 'reference', 'description')
