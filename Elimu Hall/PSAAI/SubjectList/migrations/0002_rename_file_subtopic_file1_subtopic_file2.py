# Generated by Django 4.2.3 on 2023-09-24 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SubjectList', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtopic',
            old_name='file',
            new_name='file1',
        ),
        migrations.AddField(
            model_name='subtopic',
            name='file2',
            field=models.FileField(default='start.mp4', upload_to='studyFiles'),
        ),
    ]
