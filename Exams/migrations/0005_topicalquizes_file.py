# Generated by Django 4.2.3 on 2023-09-20 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exams', '0004_classteststudenttest_is_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='topicalquizes',
            name='file',
            field=models.FileField(null=True, upload_to='media/question_files/'),
        ),
    ]
