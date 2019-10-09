# Generated by Django 2.2.1 on 2019-10-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0002_auto_20191007_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_user',
            name='email',
            field=models.EmailField(blank=True, max_length=244),
        ),
        migrations.AlterField(
            model_name='new_user',
            name='firstname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='new_user',
            name='img',
            field=models.ImageField(blank=True, max_length=1000, upload_to=''),
        ),
        migrations.AlterField(
            model_name='new_user',
            name='lastname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='new_user',
            name='password',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='new_user',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
