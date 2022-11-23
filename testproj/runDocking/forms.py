# importing the graph_input model into our form so we can start using it
from django import forms
from .models import docking_input
from django.forms import ModelForm
from .models import *



class UploadPdbForm(forms.ModelForm): 
  
    class Meta: 
        model = docking_input 
        fields = ['title', 'pdb_file', 'option1', 'option2', 'option3', 'option4']
        #fields = '__all__' 

        #def __init__(self, *args, **kwargs):
        #    super(UploadImageForm, self).__init__(*args, **kwargs)
        #    self.fields['title'].required = False
