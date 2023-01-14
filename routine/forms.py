from django import forms
from django.core.exceptions import ValidationError

from routine.models import Room, Building, SlotMaster, SlotDetail, Routine

from tempus_dominus.widgets import TimePicker, DatePicker


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = '__all__'


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('building', 'room_number', 'capacity', 'type', 'department')


class SlotMasterForm(forms.ModelForm):
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
        model = SlotMaster
        fields = ('type', 'start_effect_date', 'end_effect_date', 'status', 'short_description')


class SlotDetailForm(forms.ModelForm):
    start_time = forms.TimeField(
        widget=TimePicker(
            options={
                'format': 'HH:mm',
                'useCurrent': False,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-clock',
                'icon_toggle': True,
                'input_toggle': True,
                'placeholder': 'Start Time',
                'required': 'true',
                'autocomplete': 'off',
            },
        ),
    )

    end_time = forms.TimeField(
        widget=TimePicker(
            options={
                'format': 'HH:mm',
                'useCurrent': False,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-clock',
                'icon_toggle': True,
                'input_toggle': True,
                'placeholder': 'End Time',
                'required': 'true',
                'autocomplete': 'off',
            },
        ),
    )

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
        required=False
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
        ),
        required=False
    )

    class Meta:
        model = SlotDetail
        fields = ('slot', 'start_time', 'end_time', 'start_effect_date', 'end_effect_date')


class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['slot', 'room', 'course_dist', 'day_of_week']

    def clean(self):
        cd = self.cleaned_data
        rc = Routine.objects.filter(
            slot=cd.get('slot'),
            day_of_week=cd.get('day_of_week'),
            room=cd.get('room')
        )
        if rc:
            raise ValidationError("Room is equipped already in the given day and time")

        dist = cd.get('course_dist')

        while dist.parent_dist != dist:
            dist = dist.parent_dist

        cd['course_dist'] = dist

        for child in dist.child_dists.all():
            qs = Routine.objects.filter(
                course_dist__section=child.section,
                slot=cd.get('slot'),
                day_of_week=cd.get('day_of_week')
            )
            for data in qs:
                qd = data.course_dist.section_details
                cd = child.section_details
                if cd.starting_id == "*" or qd.starting_id == "*":
                    raise ValidationError("Student are engaged already in different classroom.")
                else:
                    if not (cd.ending_id < qd.starting_id or cd.starting_id > qd.ending_id):
                        raise ValidationError("Student are engaged already in different classroom.")

        teacher = dist.teacher

        qs = Routine.objects.filter(course_dist__teacher=teacher, slot=cd.get('slot'),
                                    day_of_week=cd.get('day_of_week'))
        if qs:
            raise ValidationError("Teacher is already engage in different classroom.")
        return cd

    def save(self, commit=True):
        i = 0
        instance = None
        cd = self.cleaned_data
        for dist in cd.get('course_dist').child_dists.all():
            ins = Routine.objects.create(
                slot=cd.get('slot'),
                room=cd.get('room'),
                day_of_week=cd.get('day_of_week'),
                course_dist=dist
            )
            if i == 0:
                instance = ins
            i += 1
        return instance


class DummyRoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['slot', 'room', 'dummy_department', 'day_of_week']




