# Generated by Django 4.2.3 on 2023-09-18 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SubjectList', '0002_topic_test_size_topic_time'),
        ('Exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentknecexams',
            name='exam_type',
            field=models.CharField(choices=[('Topical', 'Topical'), ('General', 'General'), ('Retake', 'Retake'), ('KNEC', 'KNEC')], default='Topical', max_length=10),
        ),
        migrations.AddField(
            model_name='studenttest',
            name='exam_type',
            field=models.CharField(choices=[('Topical', 'Topical'), ('General', 'General'), ('Retake', 'Retake'), ('KNEC', 'KNEC')], default='Topical', max_length=10),
        ),
        migrations.AlterField(
            model_name='studenttest',
            name='topic',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='SubjectList.topic'),
            preserve_default=False,
        ),
    ]