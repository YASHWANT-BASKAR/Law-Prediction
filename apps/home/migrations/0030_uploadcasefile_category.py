# Generated by Django 3.2.6 on 2022-08-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_uploadcasefile_uploadfile_short_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadcasefile',
            name='category',
            field=models.CharField(choices=[('Criminal Matters', 'Criminal Matters'), ('Land Acquisition', 'Land Acquisition'), ('Labour Matters', 'Labour Matters'), ('Family courts', 'Family courts'), ('Petty Cases', 'Petty Cases')], default='None', max_length=24),
        ),
    ]
