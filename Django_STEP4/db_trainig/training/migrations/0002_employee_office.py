# Generated by Django 4.0.3 on 2022-06-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='office',
            field=models.ManyToManyField(blank=True, to='training.office'),
        ),
    ]