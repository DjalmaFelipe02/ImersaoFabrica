from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'note','age','period']
        label = {
        'name': 'Nome',
        'note': 'Nota',
        'age': 'Idade',
        'period':'Período',
        }