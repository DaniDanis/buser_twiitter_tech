from django import forms
from contas.models import Profile

class Profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['foto_perfil']