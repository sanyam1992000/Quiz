# Generated by Django 2.2 on 2020-04-11 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200411_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.CharField(default=1, max_length=10000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='ques',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='weightage',
            field=models.PositiveIntegerField(default='fgude'),
            preserve_default=False,
        ),
    ]
