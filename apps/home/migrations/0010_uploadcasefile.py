# Generated by Django 3.2.6 on 2022-08-10 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_sec'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadCaseFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadfile', models.FileField(upload_to='archives/')),
            ],
        ),
    ]
