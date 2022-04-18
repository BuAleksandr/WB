# Generated by Django 3.2.9 on 2022-04-18 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('name', models.TextField()),
                ('count', models.IntegerField()),
                ('distance', models.FloatField()),
            ],
            options={
                'db_table': 'WelBeX',
                'managed': True,
            },
        ),
    ]
