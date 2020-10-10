from django.forms import ModelForm, TextInput, Select, DateInput, TimeInput
from django.utils.translation import gettext_lazy as _

from .models import Invite


class InviteForm(ModelForm):
    class Meta:
        model = Invite
        fields = [
            'name',
            'age',
            'invite_template',
            'date',
            'start_time',
            'end_time',
            'maximum_guests',
        ]
        labels = {
            'name': _('Nome'),
            'age': _('Idade'),
            'invite_template': _('Modelo'),
            'date': _('Data'),
            'start_time': _('Hora início'),
            'end_time': _('Hora fim'),
        }
        help_texts = {
            'name': _('Digite o nome que deve aparecer no convite'),
            'age': _('Digite a idade do aniversariante, ou 0 (zero) para chá de revelação'),
        }

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'age': TextInput(attrs={'class': 'form-control'}),
            'invite_template': Select(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control'}),
            'start_time': TimeInput(attrs={'class': 'form-control'}),
            'end_time': TimeInput(attrs={'class': 'form-control'}),
            'maximum_guests': TextInput(attrs={'class': 'form-control'}),
        }
