# Generated by Django 2.2 on 2020-04-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='core.Tag'),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(choices=[(models.CharField(blank=True, max_length=10000, null=True), 'option 1'), (models.CharField(blank=True, max_length=10000, null=True), 'option 2'), (models.CharField(blank=True, max_length=10000, null=True), 'option 3'), (models.CharField(blank=True, max_length=10000, null=True), 'option 4')], max_length=10000),
        ),
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='core.Tag'),
        ),
        migrations.AlterField(
            model_name='test',
            name='total_ques',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
