# Generated by Django 4.2 on 2023-04-26 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_auto_20220428_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='EIRcode1',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='EIRcode2',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='bags_no',
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]