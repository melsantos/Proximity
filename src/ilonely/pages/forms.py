from django import forms
from postman.forms import *
from django import forms

from pages.models import Document, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commentContent',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['commentContent'].widget.attrs.update({'class':'form-control'},
                                                          rows="1",
                                                          placeholder="Got something to say?",
                                                          maxlength=100)

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
