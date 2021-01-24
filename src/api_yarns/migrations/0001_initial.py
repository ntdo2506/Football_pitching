# Generated by Django 3.1.2 on 2020-10-05 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YarnsModels',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('policy', models.TextField(blank=True, null=True)),
                ('descriptions', models.TextField(blank=True, null=True)),
                ('drink', models.FloatField(default=0)),
                ('park', models.FloatField(default=0)),
                ('images', models.ManyToManyField(blank=True, null=True, related_name='image_tour', to='api_files.FilesModel')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fb_yarns',
            },
        ),
    ]
