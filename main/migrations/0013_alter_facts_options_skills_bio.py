# Generated by Django 4.2.4 on 2023-09-03 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_facts_alter_personal_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facts',
            options={'verbose_name': 'fact', 'verbose_name_plural': 'facts'},
        ),
        migrations.AddField(
            model_name='skills',
            name='bio',
            field=models.TextField(default='..', max_length=300),
        ),
    ]
