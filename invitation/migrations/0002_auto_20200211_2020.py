# Generated by Django 3.0.3 on 2020-02-11 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InviteCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='InviteTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('background_image', models.ImageField(blank=True, upload_to='', verbose_name='Background')),
                ('title_font', models.FileField(blank=True, upload_to='', verbose_name='Fonte do título')),
                ('body_font', models.FileField(blank=True, upload_to='', verbose_name='Fonte do corpo')),
                ('title_text', models.CharField(default='Título', max_length=100, verbose_name='Título')),
                ('body_text', models.TextField(default='Corpo do texto', verbose_name='Corpo do texto')),
                ('invite_data', models.TextField(blank=True, null=True, verbose_name='invite_data')),
                ('categories', models.ManyToManyField(to='invitation.InviteCategory')),
            ],
            options={
                'verbose_name': 'modelo',
                'verbose_name_plural': 'modelos',
            },
        ),
        migrations.AddField(
            model_name='invite',
            name='invite_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invitation.InviteTemplate'),
        ),
    ]
