# Generated by Django 4.0.5 on 2022-08-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_rename_statues_statutes'),
    ]

    operations = [
        migrations.AddField(
            model_name='statutes',
            name='sec_title',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
    ]
