# Generated by Django 5.1.1 on 2024-09-08 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='description',
            field=models.CharField(blank=True, max_length=1500),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
