# Generated by Django 4.2.2 on 2023-08-18 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equ', '0045_lab_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='organisation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='equ.organisation'),
        ),
    ]
