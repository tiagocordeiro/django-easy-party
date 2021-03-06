# Generated by Django 3.0.2 on 2020-01-30 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('name', models.CharField(max_length=20, verbose_name='Nome')),
                ('age', models.PositiveIntegerField(verbose_name='Idade')),
                ('gender', models.IntegerField(choices=[(0, 'Chá Revelação'), (1, 'Menino'), (2, 'Menina')], verbose_name='Genero')),
                ('date', models.DateField(verbose_name='Data')),
                ('start_time', models.TimeField(verbose_name='Hora de início')),
                ('end_time', models.TimeField(verbose_name='Hora de termino')),
                ('maximum_guests', models.PositiveIntegerField(verbose_name='Máximo de Convidados')),
            ],
            options={
                'verbose_name': 'convite',
                'verbose_name_plural': 'convites',
                'ordering': ('date', 'start_time', 'name'),
            },
        ),
        migrations.CreateModel(
            name='GuestInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nome do Convidado')),
                ('invite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invitation.Invite')),
            ],
            options={
                'verbose_name': 'convidado',
                'verbose_name_plural': 'convidados',
                'ordering': ('name',),
            },
        ),
    ]
