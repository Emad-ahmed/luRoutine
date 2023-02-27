from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.models import AbstractTimestampModel


class Faculty(AbstractTimestampModel):
    title = models.CharField(verbose_name=_(
        'Title'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _('Faculties')
    
    
    def __str__(self) -> str:
        return self.title

class FacultyDean(AbstractTimestampModel):
    faculty = models.ForeignKey(
        verbose_name=_('Faculty'),
        to='faculty.Faculty',
        related_name='deans',
        on_delete=models.CASCADE
    )
    dean = models.CharField(verbose_name=_('Faculty dean'), max_length=256)
    status = models.BooleanField(verbose_name=_('Status'), default=True)
    # date_of_joining = models.DateField(verbose_name=_('Date of Joining'), default=timezone.now())

    class Meta:
        verbose_name = _('Faculty Dean')
        verbose_name_plural = _('Faculty Deans')

    def __str__(self):
        return self.dean
    


class Department(AbstractTimestampModel):
    department_id = models.CharField(verbose_name=_(
        'Short Code'), max_length=32, unique=True)
    title = models.CharField(verbose_name=_(
        'Title'), max_length=255, unique=True)
    faculty = models.ForeignKey(
        verbose_name=_('Faculty'),
        to='faculty.Faculty',
        related_name='departments',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    def __str__(self):
        return f'{self.department_id}'


class DepartmentHead(AbstractTimestampModel):
    department = models.ForeignKey(
        verbose_name=_('Department'),
        to='faculty.Department',
        related_name='heads',
        on_delete=models.CASCADE
    )
    head = models.CharField(verbose_name=_('Head'), max_length=256)
    status = models.BooleanField(verbose_name=_('Status'), default=True)
    # date_of_joining = models.DateField(verbose_name=_('Date of Joining'), default=timezone.now())

    class Meta:
        verbose_name = _('Department Head')
        verbose_name_plural = _('Department Heads')


    def __str__(self) -> str:
        return self.head

class Program(AbstractTimestampModel):
    program_id = models.CharField(verbose_name=_(
        'Short Code'), max_length=32, unique=True)
    title = models.CharField(verbose_name=_('Program'), max_length=255)
    department = models.ForeignKey(
        verbose_name=_('Department'),
        to='faculty.Department',
        related_name='programs',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')


    def __str__(self) -> str:
        return self.title

class Curriculum(AbstractTimestampModel):
    program = models.ForeignKey(
        verbose_name=_('Program'),
        to='faculty.Program',
        related_name='curriculums',
        on_delete=models.CASCADE,
    )
    total_credit = models.FloatField(verbose_name=_('Total Credit'))
    start_effect_date = models.DateField(verbose_name=_('Start Effect Date'))
    end_effect_date = models.DateField(verbose_name=_(
        'End Effect Date'), null=True, blank=True)
    active = models.BooleanField(verbose_name=_('Active'))


    def __str__(self) -> str:
        return f"{self.program.title} - {self.id}"

class Teacher(AbstractTimestampModel):
    class FacultyType(models.TextChoices):
        PERMANENT = 'permanent', _('Permanent')
        Other = 'other', _('other')

    teacher_id = models.CharField(verbose_name=_(
        'Teacher ID'), max_length=255, unique=True)
    first_name = models.CharField(verbose_name=_('First Name'), max_length=128)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=128)
    name_initials = models.CharField(verbose_name=_(
        'Name Initials'), max_length=32, unique=True)
    department = models.ForeignKey(
        verbose_name=_('Department'),
        to='faculty.Department',
        related_name='teachers',
        on_delete=models.CASCADE,
        null=True
    )
    designation = models.CharField(
        verbose_name=_('Designation'), max_length=255)
    type = models.CharField(
        verbose_name=_('Faculty Type'),
        choices=FacultyType.choices,
        max_length=12,
        default='permanent'
    )
    contact_number = models.CharField(
        verbose_name=_('Contact Number'), max_length=20)
    email = models.EmailField(verbose_name=_('Email'))
    contact_hour = models.FloatField(verbose_name=_('Contact Hour'))

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(AbstractTimestampModel):
    class Type(models.TextChoices):
        THEORY = 'theory', _("Theory")
        LAB = 'lab', _("Lab")

    course_code = models.CharField(verbose_name=_(
        "Course Code"), max_length=16, unique=True)
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    credit = models.FloatField(verbose_name=_("Credit"))
    # program = models.ForeignKey(
    #     verbose_name=_("Program"),
    #     to="faculty.Program",
    #     related_name="courses",
    #     on_delete=models.DO_NOTHING,
    #     null=True
    # )
    curriculum = models.ManyToManyField(
        verbose_name=_('Curriculum'),
        to="faculty.Curriculum",
        related_name="courses"
    )
    pre_req = models.ForeignKey(
        verbose_name=_("Pre Req"),
        to="faculty.Course",
        related_name="dependents",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    contact_hour = models.FloatField(verbose_name=_("Contact Hour"))
    type = models.CharField(
        verbose_name=_("Type"),
        choices=Type.choices,
        max_length=8
    )

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __str__(self):
        return f"{self.id} - {self.course_code}"
