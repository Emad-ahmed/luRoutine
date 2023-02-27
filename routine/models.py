from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import AbstractTimestampModel


class Building(AbstractTimestampModel):
    title = models.CharField(verbose_name=_('Title'), max_length=255)

    class Meta:
        verbose_name = _('Building')
        verbose_name_plural = _('Buildings')


    def __str__(self) -> str:
        return self.title

class Room(AbstractTimestampModel):
    class RoomType(models.TextChoices):
        REGULAR = 'regular', _('Regular')
        LAB = 'lab', _('Lab')

    building = models.ForeignKey(
        verbose_name=_('Building'),
        to='routine.Building',
        related_name='rooms',
        on_delete=models.CASCADE,
        null=True
    )
    room_number = models.CharField(
        verbose_name=_('Room Number/ Name'), max_length=32)
    capacity = models.IntegerField(verbose_name=_('Room Number'))
    type = models.CharField(
        verbose_name=_('Type'),
        choices=RoomType.choices,
        max_length=10
    )
    department = models.ForeignKey(
        verbose_name=_('Department'),
        to='faculty.Department',
        related_name='rooms',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')

    def __str__(self):
        return self.room_number


class SlotMaster(AbstractTimestampModel):
    class Status(models.TextChoices):
        ACTIVE = 'active', _('Active'),
        INACTIVE = 'inactive', _('inactive')
    type = models.CharField(verbose_name=_('Title'), max_length=128)
    start_effect_date = models.DateField(verbose_name=_('Start Effect Date'))
    end_effect_date = models.DateField(verbose_name=_('End Effect Date'))
    short_description = models.TextField(
        verbose_name=_('Short Description'), blank=True)
    status = models.CharField(
        verbose_name=_('Status'),
        max_length=16,
        choices=Status.choices,
        default='active'
    )

    class Meta:
        verbose_name = _('Slot Master')
        verbose_name_plural = _('Slot Masters')


    def __str__(self) -> str:
        return self.type

class SlotDetail(AbstractTimestampModel):
    slot = models.ForeignKey(
        verbose_name=_('Slot'),
        to='routine.SlotMaster',
        related_name='details',
        on_delete=models.CASCADE
    )
    start_time = models.TimeField(verbose_name=_('Start Time'))
    end_time = models.TimeField(verbose_name=_('End Time'))

    class Meta:
        verbose_name = _('Slot Detail')
        verbose_name_plural = _('Slot Details')

    

    def __str__(self) -> str:
        return f"Start:{self.start_time} End:{self.end_time}"

class Routine(AbstractTimestampModel):
    class DayOfWeek(models.TextChoices):
        SATURDAY = 'saturday', _('Saturday')
        SUNDAY = 'sunday', _('Sunday')
        MONDAY = 'monday', _('Monday')
        TUESDAY = 'tuesday', _('Tuesday')
        WEDNESDAY = 'wednesday', _('Wednesday')
        THURSDAY = 'thursday', _('Thursday')
        FRIDAY = 'friday', _('Friday')

    slot = models.ForeignKey(
        verbose_name=_('Slot'),
        to='routine.SlotDetail',
        related_name='routines',
        on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        verbose_name=_('Room'),
        to='routine.Room',
        related_name='routines',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    course_dist = models.ForeignKey(
        verbose_name=_('Course Distribution'),
        to='semester.CourseDistribution',
        related_name='routines',
        on_delete=models.CASCADE,
        null=True
    )
    dummy_department = models.CharField(verbose_name=_(
        "Dummy Department"), max_length=128, null=True)
    day_of_week = models.CharField(
        verbose_name=_('Day of week'),
        max_length=16,
        choices=DayOfWeek.choices
    )

    # class Meta(AbstractTimestampModel.Meta):
    #     constraints = [
    #         models.UniqueConstraint(fields=['slot', 'room', 'day_of_week'], name='unique_routine')
    #     ]


    def __str__(self) -> str:
        return f"{self.slot}-{self.course_dist.offered.batch}-{self.course_dist.offered.semester}"