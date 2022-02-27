from itertools import count

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ValidationError
from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, TemplateView

from . import forms, models


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/keys')
    else:
        context = {'text': 'Войти по ключу', 'key_display': 'none', 'email_display': 'block'}
        if request.method == "POST":
            username = request.POST['username']
            key = request.POST['key']
            password = request.POST['password']

            if key != '':
                context = {'text': 'Войти по email', 'key_display': 'block', 'email_display': 'none'}
                try:
                    key = models.keys.objects.filter(number=key)
                except key.exists():
                    key = models.keys.objects.get(number=key)
                    userBd = models.AdvUser.objects.get(username=key.owner)
                    success = authenticate(username=userBd.username, password=password)
                    if success is None:
                        context['password'] = 'Неверный пароль'
                    else:
                        login(request, success)
                        return redirect('/keys')
                else:
                    context['key'] = 'Несуществующий ключ'
            elif username != '':
                context = {'text': 'Войти по ключу', 'key_display': 'none', 'email_display': 'block'}
                success = authenticate(username=username, password=password)
                if success is None:
                    context['password'] = 'Неверный пароль'
                else:
                    login(request, success)
                    return redirect('/keys')
            else:
                context['username'] = 'Обязательное поле'
                context['key'] = 'Обязательное поле'
        return render(request, 'user/login.html', context)


class logout(LoginRequiredMixin, LogoutView):
    template_name = 'user/logout.html'
    login_url = '/'


class createUser(CreateView):
    model = models.AdvUser
    template_name = 'user/createUser.html'
    form_class = forms.RegisterUserForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = user.username
        name = user.username
        user.save()
        userNow = models.AdvUser.objects.get(username=name)
        tariff = models.tariffs.objects.get(pk=1)
        models.keys.objects.create(number=user.key, owner=userNow, tariff=tariff)
        return super().form_valid(form)


def main(request):
    return render(request, 'index.html')


class key(LoginRequiredMixin, TemplateView):
    template_name = 'pages/keys.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_keys'] = models.keys.objects.filter(owner=self.request.user.username)
        context['tariffs'] = models.tariffs.objects.all()
        current_time = datetime.now()
        day = current_time.strftime("%d")
        month = int(current_time.strftime("%m"))+1
        if month//10 == 0:
            month = f'0{month}'
        year = current_time.strftime("%Y")
        context['first_date'] = f'{day}.{month}.{year}'
        return context


class req(LoginRequiredMixin, TemplateView):
    template_name = 'pages/req.html'
    login_url = '/'


def validateKey(request):
    context = {}
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            typeQ = request.GET.get('type')
            if typeQ == '1':
                num = request.GET.get('key')
                if models.keys.objects.filter(number=num, owner='Отсутствует').exists():
                    context['success'] = 1
                else:
                    context['success'] = 0
            else:
                num = request.GET.get('key')
                check = request.GET.get('check')
                if models.keys.objects.filter(number=num, checkNum=check, owner='Отсутствует').exists():
                    kye = models.keys.objects.get(number=num, checkNum=check)
                    kye.owner = request.user
                    kye.save()
                    context['success'] = 1
                else:
                    context['success'] = 0
    return render(request, 'user/validateKey.html', context)


def dellKey(request):
    context = {}
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            delKeys = request.GET.get('delKeys')
            delKeys = delKeys.split(';')
            for dels in delKeys:
                if models.keys.objects.filter(number=dels).exists():
                    kye = models.keys.objects.get(number=dels)
                    user = models.user.objects.get(username='Отсутствует')
                    kye.owner = user
                    kye.save()
                    context['success'] = 1
                else:
                    context['success'] = 0
    return render(request, 'user/dellKey.html', context)
