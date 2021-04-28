# Generated by Django 3.2 on 2021-04-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('released_on', models.DateField()),
                ('genre', models.CharField(max_length=250)),
                ('director', models.CharField(max_length=250)),
            ],
        ),
    ]
