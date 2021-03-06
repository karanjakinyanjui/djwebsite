# Generated by Django 2.0.5 on 2018-09-01 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to='pics')),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('facebook', models.URLField(null=True)),
                ('beatport', models.URLField(null=True)),
                ('soundcloud', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
                ('youtube', models.URLField(null=True)),
                ('twitter', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='Event')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('venue', models.CharField(max_length=140)),
                ('slug', models.SlugField(unique=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-start',),
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MixTape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='Title')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('uploaded', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-uploaded',),
            },
        ),
        migrations.CreateModel(
            name='MyPics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(null=True, upload_to='pics')),
                ('uploaded', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('mixtape_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.MixTape')),
                ('file', models.FileField(null=True, upload_to='audio')),
            ],
            options={
                'verbose_name_plural': 'Audio',
            },
            bases=('core.mixtape',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('mixtape_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.MixTape')),
                ('file', models.FileField(null=True, upload_to='video')),
            ],
            options={
                'verbose_name_plural': 'Video',
            },
            bases=('core.mixtape',),
        ),
        migrations.AddField(
            model_name='mixtape',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_core.mixtape_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='photos', to='core.MyPics'),
        ),
    ]
