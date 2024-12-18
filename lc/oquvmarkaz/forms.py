from .models import Lesson,Curs
from django import forms

class LesonForm(forms.Form):
    name=forms.CharField(max_length=150,widget=forms.TextInput(attrs={
        "placeholder": "Dars mavzusi",
        'class': "form-control"
    }))
    about=forms.CharField(required=False,widget=forms.Textarea(attrs={
        "placeholder": "Dars haqida",
        'class': "form-control",
        'rows': 3
    }))
    curs=forms.ModelMultipleChoiceField(queryset=Curs.objects.all(),
                                        widget=forms.Select(attrs={
                                            'class': 'form-select'
                                        }))
    def create(self):
        leson=Lesson.objects.create(**self.cleaned_data)
        return leson

