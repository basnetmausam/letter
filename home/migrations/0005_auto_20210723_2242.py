# Generated by Django 3.2.3 on 2021-07-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210715_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherinfo',
            name='unique_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='studentlogininfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]