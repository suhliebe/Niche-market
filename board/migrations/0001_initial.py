# Generated by Django 3.0.8 on 2020-09-02 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='TITLE')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DATE')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='MODIFY DATE')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Market')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='OWNER')),
            ],
            options={
                'verbose_name': 'board',
                'verbose_name_plural': 'boards',
                'db_table': 'board',
                'ordering': ('-modify_dt',),
            },
        ),
    ]
