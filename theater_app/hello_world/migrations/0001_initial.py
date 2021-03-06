# Generated by Django 3.0 on 2020-07-01 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='died')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a brief description of the play', max_length=1000)),
                ('actors', models.ManyToManyField(help_text='Select the actors for this play', to='hello_world.Actor')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hello_world.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a play type (e.g. Comedy, Love, History etc.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular ticket', primary_key=True, serialize=False)),
                ('date_of_play', models.DateField(blank=True, null=True)),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('play', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hello_world.Play')),
            ],
        ),
        migrations.CreateModel(
            name='PlayInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular play', primary_key=True, serialize=False)),
                ('duration', models.CharField(max_length=50)),
                ('place', models.CharField(choices=[{'Main Stage', 'MS'}, {'ES', 'Euphorion Stage'}, {'HS', 'Hamlet Stage'}], default='MS', max_length=15)),
                ('age_category', models.CharField(choices=[{'U12', 'Forbidden under 12'}, {'U14', 'Forbidden under 14'}, {'U18', 'Forbidden under 18'}], default='U12', max_length=18)),
                ('play', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hello_world.Play')),
            ],
        ),
        migrations.AddField(
            model_name='play',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hello_world.Type'),
        ),
    ]
