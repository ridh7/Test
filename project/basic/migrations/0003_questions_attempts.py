# Generated by Django 2.1.5 on 2019-02-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_remove_submissions_abc'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='attempts',
            field=models.IntegerField(default=0),
        ),
    ]