# Generated by Django 2.0.5 on 2018-09-03 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='beatport',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='soundcloud',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
    ]
