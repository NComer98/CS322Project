# Generated by Django 3.1.4 on 2020-12-03 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'account'},
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
