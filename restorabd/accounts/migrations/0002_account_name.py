# Generated by Django 2.2.4 on 2019-08-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]