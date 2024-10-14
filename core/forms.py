from django import forms
from core.models import Counterparts, Resume

class KontrForm(forms.ModelForm):

    class Meta:
        model = Counterparts
        fields = '__all__'

class ResumeForm(forms.ModelForm):

   class Meta:
      model = Resume
      fields = ['name','file']