# Generated by Django 2.0.5 on 2018-09-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180903_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone_2',
            field=models.CharField(default='0777889181', max_length=50),
            preserve_default=False,
        ),
    ]
