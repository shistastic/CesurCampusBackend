# Generated by Django 3.2.3 on 2021-05-25 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0003_alter_assignments_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='content_id',
            field=models.IntegerField(default='2'),
        ),
    ]
