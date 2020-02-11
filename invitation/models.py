from django.db import models

from core.models import Active, TimeStampedModel


class InviteCategory(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição')

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.name)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'


class InviteTemplate(Active, TimeStampedModel):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição', blank=True, null=True)
    categories = models.ManyToManyField(InviteCategory)
    background_image = models.ImageField('Background', blank=True)
    title_font = models.FileField('Fonte do título', blank=True)
    body_font = models.FileField('Fonte do corpo', blank=True)
    title_text = models.CharField('Título', default='Título', max_length=100)
    body_text = models.TextField('Corpo do texto', default='Corpo do texto')
    invite_data = models.TextField('invite_data', blank=True, null=True)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.name)

    class Meta:
        verbose_name = 'modelo'
        verbose_name_plural = 'modelos'


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
    invite_template = models.ForeignKey(InviteTemplate, on_delete=models.CASCADE, blank=True, null=True)

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
