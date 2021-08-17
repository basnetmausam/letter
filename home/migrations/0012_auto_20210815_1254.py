# Generated by Django 3.2.4 on 2021-08-15 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210812_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='project1',
            field=models.CharField(default='null', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='project2',
            field=models.CharField(default='null', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='quality',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='studentlogininfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]