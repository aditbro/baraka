# Generated by Django 2.2 on 2019-09-05 17:31

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20190905_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lowongankerja',
            name='kriteria',
        ),
        migrations.AddField(
            model_name='lowongankerja',
            name='persyaratan',
            field=djrichtextfield.models.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lowongankerja',
            name='tanggung_jawab',
            field=djrichtextfield.models.RichTextField(),
        ),
    ]