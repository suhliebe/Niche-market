# Generated by Django 3.1 on 2020-08-24 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='TITLE')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('name', models.CharField(max_length=10, verbose_name='NAME')),
            ],
            options={
                'verbose_name': 'board',
                'verbose_name_plural': 'board',
                'db_table': 'board',
            },
        ),
    ]
