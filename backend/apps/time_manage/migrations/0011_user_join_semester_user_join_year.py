# Generated by Django 4.2.4 on 2024-08-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("time_manage", "0010_alter_timetableunit_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="join_semester",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="join_year",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
