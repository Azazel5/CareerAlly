# Generated by Django 3.0.5 on 2020-04-10 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_remove_userinternshipprofile_application_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinternshipprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
