# Generated by Django 3.2.16 on 2023-02-13 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(blank=True, max_length=100, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='userprofile')),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('wallet', models.FloatField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
