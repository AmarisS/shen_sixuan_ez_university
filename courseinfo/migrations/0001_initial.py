# Generated by Django 2.1.1 on 2018-09-25 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_number', models.CharField(max_length=20)),
                ('course_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instructor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('registration_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_id', models.AutoField(primary_key=True, serialize=False)),
                ('section_name', models.CharField(max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections', to='courseinfo.Course')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections', to='courseinfo.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('semester_id', models.AutoField(primary_key=True, serialize=False)),
                ('semester_name', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('nickname', models.CharField(blank=True, max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections', to='courseinfo.Semester'),
        ),
        migrations.AddField(
            model_name='registration',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='registration', to='courseinfo.Section'),
        ),
        migrations.AddField(
            model_name='registration',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='registration', to='courseinfo.Student'),
        ),
    ]
