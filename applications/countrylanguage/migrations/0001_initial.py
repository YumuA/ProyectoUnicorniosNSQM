# Generated by Django 4.2.6 on 2023-11-30 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id_language', models.CharField(max_length=3, primary_key=True, serialize=False, verbose_name='idLanguageofcountry')),
                ('id_country', models.CharField(max_length=3, verbose_name='id country')),
                ('name_language', models.CharField(max_length=3, verbose_name='Name Language')),
            ],
            options={
                'verbose_name': 'Name Language',
                'verbose_name_plural': 'Name Languages',
                'ordering': ['name_language'],
                'unique_together': {('id_language', 'id_country')},
            },
        ),
    ]
