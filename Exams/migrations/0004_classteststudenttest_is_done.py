# Generated by Django 4.2.3 on 2023-09-18 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exams', '0003_alter_generaltest_exam_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='classteststudenttest',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
