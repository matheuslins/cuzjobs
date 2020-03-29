# Generated by Django 3.0.4 on 2020-03-29 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/assets/img/language', verbose_name='Imagem')),
                ('repositories', models.IntegerField(blank=True, null=True)),
                ('stars', models.IntegerField(blank=True, null=True)),
                ('watchers', models.IntegerField(blank=True, null=True)),
                ('forks', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
    ]