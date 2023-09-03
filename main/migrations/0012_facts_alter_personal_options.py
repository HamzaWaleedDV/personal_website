# Generated by Django 4.2.4 on 2023-09-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_personal_personal_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='personal',
            options={'verbose_name': 'Personal', 'verbose_name_plural': 'People'},
        ),
    ]
