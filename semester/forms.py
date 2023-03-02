from django import forms
from django.core.exceptions import ValidationError

from semester.models import Semester, CourseOffered, CourseDistribution, DistributedSectionDetail
from tempus_dominus.widgets import TimePicker, DatePicker


class SemesterForm(forms.ModelForm):
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
        )
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
                'required': 'true',
                'autocomplete': 'off',
            },
        )
    )

    class Meta:
        model = Semester
        fields = ('name', 'year', 'start_effect_date', 'end_effect_date')


class CourseOfferingForm(forms.ModelForm):
    class Meta:
        model = CourseOffered
        fields = '__all__'


class CourseDistributionForm(forms.ModelForm):
    starting_id = forms.CharField()
    ending_id = forms.CharField()

    class Meta:
        model = CourseDistribution
        fields = ('offered', 'section', 'teacher', 'parent_dist', 'starting_id', 'ending_id')

    def clean(self):
        cd = self.cleaned_data
        qs = CourseDistribution.objects.filter(offered=cd.get('offered'), section=cd.get('section'))
        if qs:
            for obj in qs:
                ms = DistributedSectionDetail.objects.get(distribution=obj)
                if ms.starting_id == "*" or cd.get('starting_id') == "*":
                    raise ValidationError("Course already distributed to Section.")
                else:
                    if not (cd.get('ending_id') < ms.starting_id or cd.get('starting_id') > ms.ending_id):
                        raise ValidationError("Course already distributed to Section.")
            # raise ValidationError("Course already distributed to Section.")

        parent = cd.get('parent_dist')
        if parent:
            while parent.parent_dist != parent:
                cd['parent_dist'] = parent.parent_dist
                parent = cd.get('parent_dist')

        if parent and cd.get('teacher') != parent.teacher:
            raise ValidationError("Merged sections has different teacher")

        return cd

    def save(self, commit=True):
        cd = self.cleaned_data
        instance = super(CourseDistributionForm, self).save(commit=True)
        if not instance.parent_dist:
            instance.parent_dist = instance
            instance.save()

        DistributedSectionDetail.objects.update(
            distribution=instance,
            starting_id=cd.get('starting_id'),
            ending_id=cd.get('ending_id')
        )

        return instance



class CourseDistributionUpdateForm(forms.ModelForm):
    class Meta:
        model = CourseDistribution
        fields = ('offered', 'section', 'teacher', 'parent_dist')
    def clean(self):
        cd = self.cleaned_data
        parent = cd.get('parent_dist')
        if parent:
            while parent.parent_dist != parent:
                cd['parent_dist'] = parent.parent_dist
                parent = cd.get('parent_dist')

        if parent and cd.get('teacher') != parent.teacher:
            raise ValidationError("Merged sections has different teacher")

        return cd

