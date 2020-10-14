# Generated by Django 3.1.2 on 2020-10-14 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place'),
        ),
    ]
