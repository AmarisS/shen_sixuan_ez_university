# Generated by Django 2.1.1 on 2018-10-31 05:05

from django.db import migrations, models

YEARS = [
    {
        "year": 2018,
    },
    {
        "year": 2019
    },
    {
        "year": 2020
    },
    {
        "year": 9999,
    },
]


def add_year_data(apps, schema_editor):
    year_class = apps.get_model('courseinfo', 'Year')
    for this_year in YEARS:
        year_object = year_class.objects.create(
            year=this_year['year']
        )


def remove_year_data(apps, schema_editor):
    year_class = apps.get_model('courseinfo', 'Year')
    for this_year in YEARS:
        year_object = year_class.objects.get(
            year=this_year['year']
        )
        year_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0005_period_schema_and_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('year_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField(unique=True)),
            ],
            options={
                'ordering': ['year'],
            },
        ),
        migrations.RunPython(
            add_year_data,
            remove_year_data
        )
    ]
