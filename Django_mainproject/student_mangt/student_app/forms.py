from django import forms
from.models import students

class studentform(forms.ModelForm):
    class Meta:
        model = students
        fields = ['stud_name', 'email', 'phone_no','department']
