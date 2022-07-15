from wsgiref.handlers import format_date_time
from django import forms
from pagina_web.models import Posts

class form_TextoPost(forms.Form):
    texto = forms.CharField(widget=forms.Textarea)

