# Generated by Django 3.0.4 on 2020-04-03 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_learn', '0004_auto_20200401_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='vlearnuser',
            name='firstName',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AddField(
            model_name='vlearnuser',
            name='lastName',
            field=models.CharField(max_length=264, null=True),
        ),
    ]
