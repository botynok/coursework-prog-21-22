from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from decimal import Decimal

from .forms import RegisterUserForm
from .forms import LoginUserForm
from .forms import StudentsEventForm

from .models import StudentsEvent
from .models import SportEvent
from .models import CreativeEvent
from .models import StudiesEvent
from .models import ScienceEvent
from .models import RatingTable
from .models import UserContext
from django.contrib.auth.models import User


def index(request):
    rating = RatingTable.objects.order_by('-normalized_score') # здесь можно ещё использовать all() и order_by('(-)title')[:] посмотреть гоша дударь часть с получанием и выводом данных
    return render(request, 'main/index.html', {'rating': rating})


def profile(request):
    my_profile = False
    if request.method == 'GET' and request.user.is_authenticated:
        req_id = request.GET.get('id')
        if req_id is None:
            my_profile = True
            req_user = User.objects.get(id=request.user.id)
            try:
                user_context = UserContext.objects.get(user_id=request.user.id)
            except:
                user_context = False

        else:
            req_user = User.objects.get(id=req_id)

            if int(req_id) == request.user.id:
                my_profile = True
            try:
                user_context = UserContext.objects.get(user_id=req_id)
            except:
                user_context = False
    else:
        req_user = False
        user_context = False

    context = {
        'req_user': req_user,
        'user_context': user_context,
        'my_profile': my_profile,
    }
    return render(request, 'main/profile.html', context)


def check_event(request):
    events = StudentsEvent.objects.filter(checked='Проверяется')
    return render(request, 'main/check_event.html', {'events': events})


def check_true(request):
    if request.method == 'POST':

        event = StudentsEvent.objects.filter(checked='Проверяется').get(id=request.POST['id'])
        event.checked = request.POST['decision']
        event.save()
        if request.POST['decision'] == 'Одобрено':
            score = Decimal("1.0")

            if event.level == "Университетский":
                score *= Decimal("1.2")
            elif event.level == "Городской":
                score *= 2
            elif event.level == "Всероссийский":
                score *= 3

            if event.role == "Участник":
                score *= Decimal("1.2")
            elif event.role == "Призёр":
                score *= 2
            elif event.role == "Организатор":
                score *= 2
            elif event.role == "Спикер":
                score *= 2
            elif event.role == "Победитель":
                score *= 3
            elif event.role == "Гл. Организатор":
                score *= 3

            chosen_event = ''

            if event.type == "Спортивная":
                chosen_event = SportEvent
            elif event.type == "Творческая":
                chosen_event = CreativeEvent
            elif event.type == "Учебная":
                chosen_event = StudiesEvent
            elif event.type == "Научная":
                chosen_event = ScienceEvent


            try:
                checked_event = chosen_event.objects.get(user_id=event.user_id)
                has_user = True

            except:
                has_user = False

            if has_user:
                checked_event.score += score
                checked_event.save()

            else:
                checked_event = chosen_event(title=event.name, user_id=event.user_id, score=score)
                checked_event.save()

            # добавляем пользвателя в рейтинг
            add_to_rating(event)

            # нормализуем рейтинг по каждому типу мероприятий

            chosen_event = [SportEvent, CreativeEvent, StudiesEvent, ScienceEvent]

            for eve in chosen_event:
                norm_students = eve.objects.order_by('-score')
                normalize = []
                for el in norm_students:
                    normalize.append(el.score)

                if len(normalize) != 0:

                    max_normalize = max(normalize)
                    min_normalize = min(normalize)
                    diff = max_normalize - min_normalize

                    if diff != 0:
                        for i in range(len(normalize)):
                            normalize[i] = (normalize[i] - min_normalize) / diff
                            normalize[i] = normalize[i].quantize(Decimal("1.00"))
                            norm_students[i].normalized_score = normalize[i]
                            norm_students[i].save()

            start_rating()

    return redirect('check_event')


def start_rating():

    # добавляем в общий рейтинг все события по каждому пользователю

    events = [SportEvent, CreativeEvent, StudiesEvent, ScienceEvent]

    for rating_user in RatingTable.objects.all():
        sum_score = 0
        for chosen_event in events:
            try:
                checked_event = chosen_event.objects.get(user_id=rating_user.user_id)
                sum_score += checked_event.normalized_score
            except:
                pass
        rating_user.score = sum_score
        rating_user.save()

    # нормализуем общий рейтинг

    rating_students = RatingTable.objects.order_by('-score')
    normalize = []
    for el in rating_students:
        normalize.append(el.score)

    if len(normalize) != 0:
        max_normalize = max(normalize)
        min_normalize = min(normalize)
        diff = max_normalize - min_normalize

        if diff != 0:
            for i in range(len(normalize)):
                normalize[i] = (normalize[i] - min_normalize) / diff
                normalize[i] = normalize[i].quantize(Decimal("1.00"))
                rating_students[i].normalized_score = normalize[i]
                rating_students[i].save()


    # расставляем места в RatingTable
    rating_students = RatingTable.objects.order_by('-normalized_score')
    place = 1
    for el in rating_students:
        el.place = place
        el.save()
        place += 1


def add_to_rating(event):

    chosen_event = RatingTable

    try:
        checked_event = chosen_event.objects.get(user_id=event.user_id)

    except:
        checked_event = chosen_event(title=event.name, user_id=event.user_id, score=0)
        checked_event.save()


def rating(request):
    rating = RatingTable.objects.order_by('-normalized_score')
    return render(request, 'main/rating.html', {'rating': rating})


def add_event(request):
    error = ''
    fio = ''
    if request.method == 'POST':
        post_form = StudentsEventForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_event')
        else:
            error = 'Форма была некорректной'

    if request.user.is_authenticated:
        try:
            patronymic = UserContext.objects.get(user_id=request.user.id)
            fio = request.user.last_name + ' ' + request.user.first_name + ' ' + patronymic.patronymic

        except:
            fio = request.user.last_name + ' ' + request.user.first_name

    form = StudentsEventForm()
    context = {
        'form': form,
        'error': error,
        'fio': fio
    }
    return render(request, 'main/add_event.html', context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        user_context = UserContext(user_id=user.id, phone_number=self.request.POST['phone_number'],
                                   patronymic=self.request.POST['patronymic'])
        user_context.save()

        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
