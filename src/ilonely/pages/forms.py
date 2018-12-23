from django import forms
from postman.forms import *
from django import forms

from pages.models import Document

class CustomWriteForm(WriteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recipients'].widget.attrs.update({'class':'form-control'})
        self.fields['body'].widget.attrs.update({'class':'form-control'})
        self.fields['subject'].widget.attrs.update({'class':'form-control'})

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
