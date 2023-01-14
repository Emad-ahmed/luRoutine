from django import forms
from student.models import Batch, Section


class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ('batch', 'section')
