# Generated by Django 3.1 on 2021-08-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210809_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='letter',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
    ]
