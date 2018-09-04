# Generated by Django 2.0.5 on 2018-09-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180904_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='picture',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='file',
            field=models.FileField(null=True, upload_to='audio'),
        ),
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='mixtape',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='mypics',
            name='file',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(null=True, upload_to='video'),
        ),
    ]
