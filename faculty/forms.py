from django import forms
from django.core.exceptions import ValidationError

from faculty.models import Faculty, Department, Program, Teacher, Course, Curriculum, FacultyDean, DepartmentHead
from tempus_dominus.widgets import DatePicker
from django.contrib.auth.models import User


class FacultyForm(forms.ModelForm):
    dean = forms.CharField()

    class Meta:
        model = Faculty
        fields = ('title', 'dean')

    def save(self, commit=True):
        cd = self.cleaned_data
        instance = Faculty.objects.create(title=cd.get('title'))
        FacultyDean.objects.create(faculty=instance, dean=cd.get('dean'))

        return instance


class DepartmentForm(forms.ModelForm):
    head = forms.CharField()

    class Meta:
        model = Department
        fields = ('department_id', 'title', 'faculty')

    def save(self, commit=True):
        cd = self.cleaned_data
        instance = Department.objects.create(
            title=cd.get('title'),
            department_id=cd.get('department_id'),
            faculty=cd.get('faculty')
        )
        DepartmentHead.objects.create(department=instance, head=cd.get('head'))

        return instance


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ('program_id', 'title', 'department')


class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = ('program', 'total_credit', 'start_effect_date', 'end_effect_date', 'active')

    start_effect_date = forms.DateField(
        widget=DatePicker(
            options={
                'collapse': False,
                'format': 'L',
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
                'input_toggle': True,
                'placeholder': 'Start Effect Date',
                'required': 'true',
                'autocomplete': 'off',
            },
        ),
    )

    end_effect_date = forms.DateField(
        widget=DatePicker(
            options={
                'collapse': False,
                'format': 'L',
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
                'input_toggle': True,
                'placeholder': 'End Effect Date',
                'autocomplete': 'off',
            },
        ),
        required=False,
    )


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('teacher_id', 'first_name', 'last_name', 'name_initials', 'department', 'designation', 'type',
                  'contact_number', 'email', 'contact_hour')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('curriculum', 'course_code', 'title', 'credit', 'pre_req', 'contact_hour', 'type')

    def clean(self):
        cd = self.cleaned_data
        program = None
        for cur in cd.get('curriculum'):
            if not program:
                program = cur.program
            else:
                if program != cur.program:
                    raise ValidationError("Curriculums Not from Same Program")
        return cd


class TeacherAccountCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
