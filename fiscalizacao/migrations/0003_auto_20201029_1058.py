# Generated by Django 3.1.2 on 2020-10-29 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiscalizacao', '0002_auto_20201005_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='support_case',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
