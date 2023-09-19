from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class StudentsEvent(models.Model):
    name = models.CharField('ФИО студента', max_length=50)
    user_id = models.DecimalField('ID студента', max_digits=10, decimal_places=0, default=-1)
    title = models.CharField('Название', max_length=50)
    type = models.CharField('Тип деятельности', max_length=20)  # спорт, творч, учеба
    level = models.CharField('Уровень мероприятия', max_length=20)  # универ, город, всерос
    role = models.CharField('Роль', max_length=20)  # 1,2,3 но в конечном варианте побед, призер, уч или гл орг, орг, уч
    checked = models.CharField('Статус проверки', max_length=20, default='Проверяется')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятие на проверку'
        verbose_name_plural = 'Мероприятия на проверку'

#  role = models.CharField('Роль')  # 1,2,3 но в конечном варианте побед, призер, уч или гл орг, орг, уч


class SportEvent(models.Model):
    title = models.CharField('ФИО студента', max_length=50)
    user_id = models.DecimalField('ID студента', max_digits=10, decimal_places=0)
    score = models.DecimalField('Баллы студента', max_digits=7, decimal_places=2)
    normalized_score = models.DecimalField('Пронормированные баллы студента', max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Спортивное мероприятие'
        verbose_name_plural = 'Спортивные мероприятия'


class CreativeEvent(models.Model):
    title = models.CharField('ФИО студента', max_length=50)
    user_id = models.DecimalField('ID студента', max_digits=10, decimal_places=0)
    score = models.DecimalField('Баллы студента', max_digits=7, decimal_places=2)
    normalized_score = models.DecimalField('Пронормированные баллы студента', max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Творческое мероприятие'
        verbose_name_plural = 'Творческие мероприятия'


class StudiesEvent(models.Model):
    title = models.CharField('ФИО студента', max_length=50)
    user_id = models.DecimalField('ID студента', max_digits=10, decimal_places=0)
    score = models.DecimalField('Баллы студента', max_digits=7, decimal_places=2)
    normalized_score = models.DecimalField('Пронормированные баллы студента', max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Учебное мероприятие'
        verbose_name_plural = 'Учебные мероприятия'


class ScienceEvent(models.Model):
    title = models.CharField('ФИО студента', max_length=50)
    user_id = models.DecimalField('ID студента', max_digits=10, decimal_places=0)
    score = models.DecimalField('Баллы студента', max_digits=7, decimal_places=2)
    normalized_score = models.DecimalField('Пронормированные баллы студента', max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Научное мероприятие'
        verbose_name_plural = 'Научные мероприятия'


class RatingTable(models.Model):
    title = models.CharField('ФИО студента', max_length=50)
    user_id = models.DecimalField('ID студента', max_digits=10, decimal_places=0)
    place = models.DecimalField('Место в рейтинге', max_digits=10, decimal_places=0, default=0)
    score = models.DecimalField('Баллы студента', max_digits=7, decimal_places=2)
    normalized_score = models.DecimalField('Пронормированные баллы студента', max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Общий рейтинг'
        verbose_name_plural = 'Общий рейтинг'


class UserContext(models.Model):
    user_id = models.DecimalField('ID студента', max_digits=10, decimal_places=0)
    phone_number = models.CharField('Номер телефона', max_length=20)
    patronymic = models.CharField('Отчество', max_length=20)
    likes = models.DecimalField('Лайки', max_digits=7, decimal_places=0, default=0)
    dislikes = models.DecimalField('Лайки', max_digits=7, decimal_places=0, default=0)
