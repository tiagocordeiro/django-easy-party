from django.db import models

from core.models import Active, TimeStampedModel


class Invite(Active, TimeStampedModel):
    GENDER_CHOICES = (
        (0, 'Chá Revelação'),
        (1, 'Menino'),
        (2, 'Menina'),
    )
    name = models.CharField('Nome', max_length=20)
    age = models.PositiveIntegerField('Idade')
    gender = models.IntegerField('Genero', choices=GENDER_CHOICES)
    date = models.DateField('Data')
    start_time = models.TimeField('Hora de início')
    end_time = models.TimeField('Hora de termino')
    maximum_guests = models.PositiveIntegerField('Máximo de Convidados')

    class Meta:
        ordering = ('date', 'start_time', 'name',)
        verbose_name_plural = "convites"
        verbose_name = "convite"


class GuestInvite(models.Model):
    invite = models.ForeignKey(Invite, on_delete=models.CASCADE)
    name = models.CharField('Nome do Convidado', max_length=20)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "convidados"
        verbose_name = "convidado"


class InviteTemplate(Active, TimeStampedModel):
    name = models.CharField('Nome', max_length=50)
