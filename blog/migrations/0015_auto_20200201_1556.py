# Generated by Django 2.2.6 on 2020-02-01 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200201_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='enno',
            field=models.CharField(max_length=12, null=True),
        ),
    ]