# Generated by Django 2.2.5 on 2020-01-09 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='內容')),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
