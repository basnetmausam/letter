# Generated by Django 3.1 on 2021-07-15 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210715_1209'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentEmail',
        ),
        migrations.AddField(
            model_name='studentdata',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]