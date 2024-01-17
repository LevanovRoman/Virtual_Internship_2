# Generated by Django 5.0.1 on 2024-01-17 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('height', models.IntegerField(verbose_name='Высота')),
            ],
            options={
                'verbose_name': 'Координаты',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(blank=True, max_length=2, verbose_name='Зима')),
                ('summer', models.CharField(blank=True, max_length=2, verbose_name='Лето')),
                ('autumn', models.CharField(blank=True, max_length=2, verbose_name='Осень')),
                ('spring', models.CharField(blank=True, max_length=2, verbose_name='Весна')),
            ],
            options={
                'verbose_name': 'Уровень сложности',
                'verbose_name_plural': 'Уровни сложности',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.CharField(max_length=100, verbose_name='Почта')),
                ('fam', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('otc', models.CharField(max_length=50, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=20, verbose_name='Контактный телефон')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('New', 'новый'), ('Pending', 'в работе'), ('Accepted', 'принят'), ('Rejected', 'отклонен')], default='New', max_length=10, verbose_name='Статус')),
                ('beauty_title', models.CharField(blank=True, max_length=100, verbose_name='Основное название вершины')),
                ('title', models.CharField(max_length=100, verbose_name='Название вершины')),
                ('other_titles', models.CharField(blank=True, max_length=100, verbose_name='Другое название')),
                ('connect', models.CharField(blank=True, max_length=100, verbose_name='Связывает')),
                ('add_time', models.TimeField(auto_now_add=True)),
                ('coordinates', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.coordinates', verbose_name='Координаты')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Перевал',
                'verbose_name_plural': 'Перевалы',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(blank=True, max_length=255, null=True, verbose_name='Изображение')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('pereval', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='mainapp.pereval')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
