# Generated by Django 3.2.10 on 2021-12-20 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО студента')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('kind', models.CharField(max_length=50, verbose_name='Вид деятельности')),
                ('type', models.CharField(max_length=20, verbose_name='Тип деятельности')),
                ('level', models.CharField(max_length=20, verbose_name='Уровень мероприятия')),
                ('role', models.CharField(max_length=20, verbose_name='Роль')),
                ('checked', models.CharField(max_length=20, verbose_name='Статус проверки')),
            ],
        ),
    ]
