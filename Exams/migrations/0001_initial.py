# Generated by Django 4.2.3 on 2023-09-21 16:14

import Exams.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('Users', '0001_initial'),
        ('SubjectList', '0001_initial'),
        ('Supervisor', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsKnecAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('is_correct', models.BooleanField(default=False)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KNECGradeExams',
            fields=[
                ('uuid', Exams.models.UniqueUUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('test_size', models.PositiveIntegerField()),
                ('duration', models.PositiveIntegerField(default='15')),
                ('date', models.DateTimeField()),
                ('expiry', models.DateField(null=True)),
                ('grade', models.CharField(max_length=2)),
                ('term', models.CharField(default='2', max_length=100)),
                ('year', models.CharField(default='2023', max_length=6)),
                ('quiz', models.ManyToManyField(to='Supervisor.knecquizzes')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubjectList.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TopicalQuizes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('file', models.FileField(null=True, upload_to='question_files/')),
                ('quiz', models.TextField(max_length=500)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubjectList.subject')),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubjectList.subtopic')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubjectList.topic')),
            ],
        ),
        migrations.CreateModel(
            name='TopicalQuizAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('choice', models.CharField(max_length=600)),
                ('is_correct', models.BooleanField(default=False)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exams.topicalquizes')),
            ],
        ),
        migrations.CreateModel(
            name='StudentTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', Exams.models.UniqueUUIDField(default=uuid.uuid4, unique=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('marks', models.CharField(default='0', max_length=100)),
                ('exam_type', models.CharField(choices=[('Topical', 'Topical'), ('General', 'General'), ('Retake', 'Retake'), ('KNEC', 'KNEC')], default='Topical', max_length=10)),
                ('test_size', models.PositiveIntegerField(default=15)),
                ('duration', models.PositiveIntegerField(default=15)),
                ('quiz', models.ManyToManyField(to='Exams.topicalquizes')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubjectList.subject')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubjectList.topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', Exams.models.UniqueUUIDField(default=uuid.uuid4, unique=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('marks', models.CharField(default='0', max_length=100)),
                ('exam_type', models.CharField(choices=[('Topical', 'Topical'), ('General', 'General'), ('Retake', 'Retake'), ('KNEC', 'KNEC')], default='Topical', max_length=10)),
                ('test_size', models.PositiveIntegerField(default=15)),
                ('duration', models.PositiveIntegerField(default=15)),
                ('quiz', models.ManyToManyField(to='Exams.topicalquizes')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubjectList.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClassTest',
            fields=[
                ('uuid', Exams.models.UniqueUUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('test_size', models.PositiveIntegerField()),
                ('duration', models.PositiveIntegerField(default='15')),
                ('date', models.DateTimeField()),
                ('expiry', models.DateField(null=True)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.schoolclass')),
                ('quiz', models.ManyToManyField(to='Exams.topicalquizes')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubjectList.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentsAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('test_object_id', models.UUIDField()),
                ('is_correct', models.BooleanField(default=False)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exams.topicalquizes')),
                ('selection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exams.topicalquizanswers')),
                ('test_content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'uuid')},
            },
        ),
        migrations.CreateModel(
            name='StudentKNECExams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(choices=[('Topical', 'Topical'), ('General', 'General'), ('Retake', 'Retake'), ('KNEC', 'KNEC')], default='Topical', max_length=10)),
                ('test_size', models.PositiveIntegerField(default=15)),
                ('duration', models.PositiveIntegerField(default=15)),
                ('uuid', models.CharField(default=uuid.uuid4, max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('marks', models.CharField(default='0', max_length=100)),
                ('finished', models.BooleanField(default=False)),
                ('quiz', models.ManyToManyField(to='Exams.topicalquizes')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubjectList.subject')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exams.knecgradeexams')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'uuid')},
            },
        ),
        migrations.CreateModel(
            name='ClassTestStudentTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=uuid.uuid4, max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('marks', models.CharField(default='0', max_length=100)),
                ('is_done', models.BooleanField(default=False)),
                ('finished', models.BooleanField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exams.classtest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'uuid')},
            },
        ),
    ]
