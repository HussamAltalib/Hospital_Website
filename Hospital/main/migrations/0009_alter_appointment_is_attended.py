# Generated by Django 4.1.7 on 2023-02-18 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_clinic_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='is_attended',
            field=models.BooleanField(default=False),
        ),
    ]
