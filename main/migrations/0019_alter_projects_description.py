# Generated by Django 4.2.4 on 2023-09-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_skills_desc_for_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(max_length=5000),
        ),
    ]
