# Generated by Django 4.1.2 on 2022-10-16 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='subtitle',
            field=models.CharField(max_length=200, null=True),
        ),
    ]