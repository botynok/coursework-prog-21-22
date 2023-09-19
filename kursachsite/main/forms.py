from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import StudentsEvent


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control w-50', 'id': 'floatingInput',
                                                                            'placeholder': "name@example.com"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control w-50', 'id': 'floatingInput',
                                                                            'placeholder': "name@example.com"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control w-50', 'id': 'floatingInput',
                                                                            'placeholder': "name@example.com"}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control w-50', 'id': 'floatingInput',
                                                                            'placeholder': "name@example.com"}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control w-50', 'id': 'floatingInput',
                                                                            'placeholder': "name@example.com"}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control w-50', 'id': 'floatingInput',
                                                                            'placeholder': "name@example.com"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control w-50', 'id': 'floatingInput',
                                                                            'placeholder': "name@example.com"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control w-50', 'id': 'floatingInput',
                                                                            'placeholder': "name@example.com"}))


class StudentsEventForm(ModelForm):
    CHOICE_TYPE = [('Спортивная', 'Спортивное'), ('Творческая', 'Творческое'),
                   ('Учебная', 'Учебное'), ('Научная', 'Научное')]
    CHOICE_LEVEL = [('Университетский', 'Университетский'),
                    ('Городской', 'Городской'), ('Всероссийский', 'Всероссийский')]
    CHOICE_ROLE = [('Участник', 'Участник'), ('Гл. Организатор', 'Гл. Организатор'),
                   ('Организатор', 'Организатор'), ('Победитель', 'Победитель'),
                   ('Призёр', 'Призёр'), ('Спикер', 'Спикер')]

    name = ''
    title = forms.CharField(label='Название мероприятия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    type = forms.ChoiceField(label='Тип мероприятия', choices=CHOICE_TYPE, widget=forms.Select(attrs={'class': 'form-input'}))
    level = forms.ChoiceField(label='Уровень мероприятия', choices=CHOICE_LEVEL, widget=forms.Select(attrs={'class': 'form-input'}))
    role = forms.ChoiceField(label='Роль на мероприятии', choices=CHOICE_ROLE, widget=forms.Select(attrs={'class': 'form-input'}))
    user_id = -2

    class Meta:
        model = StudentsEvent
        fields = ["name", "title", "type", "level", "role", "user_id"]
