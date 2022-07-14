from django.forms.models import ModelForm
from pagina_web.models import Posts

class FormPost(ModelForm):
   class Meta:
       model = Posts
       fields = '__all__'
       exclude = ('user','data')