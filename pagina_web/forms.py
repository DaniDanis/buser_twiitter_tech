from django import forms


class form_TextoPost(forms.Form):
    texto = forms.CharField(widget=forms.Textarea)
