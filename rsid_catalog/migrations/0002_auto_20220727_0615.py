# Generated by Django 3.0 on 2022-07-27 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rsid_catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='user',
        ),
        migrations.AddField(
            model_name='rsids',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rsid', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]