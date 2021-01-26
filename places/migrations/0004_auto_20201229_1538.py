# Generated by Django 3.1.2 on 2020-12-29 12:38

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20201229_1529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['picture_index'], 'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['title'], 'verbose_name': 'Расположение', 'verbose_name_plural': 'Расположения'},
        ),
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
    ]