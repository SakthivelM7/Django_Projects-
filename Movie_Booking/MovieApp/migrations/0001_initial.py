# Generated by Django 4.2.6 on 2023-11-17 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Heroin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heroin_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mov_name', models.CharField(max_length=150)),
                ('cost', models.IntegerField()),
                ('director_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieApp.director')),
                ('hero_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieApp.hero')),
                ('heroin_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieApp.heroin')),
            ],
        ),
    ]