from django.db import models
from core.models import AbstractTimestampModel
from django.utils.translation import gettext_lazy as _


class Batch(AbstractTimestampModel):
    batch = models.IntegerField(verbose_name=_("Batch"))
    # program = models.ForeignKey(
    #     verbose_name=_("Program"),
    #     to="faculty.Program",
    #     related_name='batches',
    #     on_delete=models.DO_NOTHING
    # )
    curriculum = models.ForeignKey(
        verbose_name=_("Curriculum"),
        to="faculty.Curriculum",
        related_name="batches",
        on_delete=models.DO_NOTHING
    )
    # start_effect_date = models.DateField(verbose_name=_('Start Effect Date'), null=True)

    class Meta:
        verbose_name = _('Batch')
        verbose_name_plural = _('Batches')


class Section(AbstractTimestampModel):
    batch = models.ForeignKey(
        verbose_name=_('Batch'),
        to="student.Batch",
        related_name="sections",
        on_delete=models.DO_NOTHING
    )
    section = models.CharField(verbose_name=_("Section"), max_length=64)
    parent_section = models.ForeignKey(
        verbose_name=_("Parent Section"),
        to="student.Section",
        related_name="child_sections",
        on_delete=models.DO_NOTHING,
        null=True
    )

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
