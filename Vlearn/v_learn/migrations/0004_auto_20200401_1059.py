# Generated by Django 3.0.4 on 2020-04-01 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_learn', '0003_vlearnuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vlearnuser',
            name='courseList',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='vlearnuser',
            name='emailid',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='vlearnuser',
            name='percentage',
            field=models.CharField(max_length=264, null=True),
        ),
    ]
