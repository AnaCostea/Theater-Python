# Generated by Django 3.0 on 2020-07-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0004_auto_20200701_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playinfo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
