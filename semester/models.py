from django.db import models
from core.models import AbstractTimestampModel
from django.utils.translation import gettext_lazy as _




class Semester(AbstractTimestampModel):
    class Name(models.TextChoices):
        SUMMER = 'summer', _('Summer')
        FALL = 'fall', _('Fall')
        SPRING = 'spring', _('Spring')

    name = models.CharField(
        verbose_name=_('Name'),
        choices=Name.choices,
        max_length=8
    )
    year = models.IntegerField(verbose_name=_('Year'))
    start_effect_date = models.DateField(
        verbose_name=_('Start Effect Date'), null=True)
    end_effect_date = models.DateField(
        verbose_name=_('End Effect Date'), null=True)
    status = models.BooleanField(verbose_name=_("Status"), default=True)

    class Meta:
        verbose_name = _('Semester')
        verbose_name_plural = _('Semesters')

    def __str__(self) -> str:
        return f"{self.id}- {self.name}"


class CourseOffered(AbstractTimestampModel):
    semester = models.ForeignKey(
        verbose_name=_('Semester'),
        to='semester.Semester',
        related_name='offered',
        on_delete=models.CASCADE
    )
    
    batch = models.ForeignKey(
        verbose_name=_('Batch'),
        to='student.Batch',
        related_name='offered',
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        verbose_name=_('Course'),
        to='faculty.Course',
        related_name='offered',
        on_delete=models.CASCADE
    )

    # class Meta:
    #     verbose_name = _('Course Offered')
    #     verbose_name_plural = _('Courses Offered')
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['semester', 'batch', 'course'], name='unique_offering')
    #     ]
    
    def __str__(self):
        return f"Id: {self.semester.name}[{self.semester.id}],Batch Id:{self.batch.batch}[{self.batch.id}], Course Id: {self.course.course_code}[{self.course.id}]"





class CourseDistribution(AbstractTimestampModel):

    offered = models.ForeignKey(
        verbose_name=_('Course Offered'),
        to='semester.CourseOffered',
        related_name='distributions',
        on_delete=models.CASCADE
    )

    section = models.ForeignKey(
        verbose_name=_('Sections'),
        to='student.Section',
        related_name='distributions',
        on_delete=models.CASCADE
    )
    teacher = models.ForeignKey(
        verbose_name=_('Teacher'),
        to='faculty.Teacher',
        related_name='distributions',
        on_delete=models.DO_NOTHING
    )
    parent_dist = models.ForeignKey(
        verbose_name=_("Parent Distribution"),
        to='semester.CourseDistribution',
        related_name='child_dists',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Course Distribution')
        verbose_name_plural = _('Course Distributions')
        # constraints = [
        #     models.UniqueConstraint(fields=['offered', 'section', 'teacher'], name='unique_distribution')
        # ]
    def __str__(self) -> str:
        return f"{self.offered.batch.batch}-{self.section.section}"






class DistributedSectionDetail(AbstractTimestampModel):
    distribution = models.OneToOneField(
        verbose_name=_('Distributed Course'),
        to='semester.CourseDistribution',
        related_name='section_details',
        on_delete=models.CASCADE
    )
    starting_id = models.CharField(verbose_name=_(
        'Starting ID'), max_length=16, default='*')
    ending_id = models.CharField(verbose_name=_(
        'Ending ID'), max_length=16, default='*')
