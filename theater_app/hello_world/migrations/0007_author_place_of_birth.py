# Generated by Django 3.0 on 2020-07-01 16:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0006_auto_20200701_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='place_of_birth',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
