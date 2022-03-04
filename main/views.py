from django.core.exceptions import ValidationError
from django.core.signing import BadSignature
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, TemplateView, FormView
from django.views.generic.list import ListView
from . import forms, models, utilities


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
    next_page = '/'


class createUser(CreateView):
    model = models.AdvUser
    template_name = 'user/createUser.html'
    form_class = forms.RegisterUserForm
    success_url = '/'


class key(LoginRequiredMixin, TemplateView):
    template_name = 'pages/keys.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_keys'] = models.keys.objects.filter(owner=self.request.user.username)
        context['tariffs'] = models.tariffs.objects.all()
        current_time = datetime.now()
        day = current_time.strftime("%d")
        month = int(current_time.strftime("%m")) + 1
        if month // 10 == 0:
            month = f'0{month}'
        year = current_time.strftime("%Y")
        context['first_date'] = f'{day}.{month}.{year}'
        return context


class req(LoginRequiredMixin, TemplateView):
    template_name = 'pages/req.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_req'] = models.requisites.objects.filter(owner=self.request.user.username)
        return context

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
            elif typeQ == '0':
                num = request.GET.get('key')
                check = request.GET.get('check')
                if models.keys.objects.filter(number=num, checkNum=check, owner='Отсутствует').exists():
                    kye = models.keys.objects.get(number=num, checkNum=check)
                    kye.owner = request.user
                    kye.save()
                    context['success'] = 1
                else:
                    context['success'] = 0
            elif typeQ == '2':
                delKeys = request.GET.get('delKeys')
                delKeys = delKeys.split(';')
                context['success'] = delKeys
                for dels in delKeys:
                    context['success'] = dels
                    if dels != '':
                        if models.keys.objects.filter(number=dels).exists():
                            kye = models.keys.objects.get(number=dels)
                            user = models.AdvUser.objects.get(pk=6)
                            kye.owner = user
                            kye.save()
                context['success'] = 1
    return render(request, 'user/validateKey.html', context)


def password_email_form(request):
    context = {'display': 'none'}
    if request.method == "POST":
        username = request.POST['username']
        if models.AdvUser.objects.filter(username=username).exists():
            user = models.AdvUser.objects.get(username=username)
            utilities.send_password_notification(user)
            context['mail'] = "Проверьте почту"
            context['display'] = 'block'
        else:
            context['errors'] = "Введен неверный логин"
    return render(request, 'user/password_email_form.html', context)


def password_email(request, sign):
    context = {}
    username = utilities.signer.unsign(sign)
    user = get_object_or_404(models.AdvUser, username=username)
    if request.method == 'post':
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            user.set_password(password)
            user.save()
            template = 'user/password_change_email_done.html'
        else:
            context['errors'] = "Пароли не совпадают"
    else:
        template = 'user/password_change_email.html'

    return render(request, template, context)


class checks(ListView):
    model = models.checks
    template_name = 'pages/checks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_checks'] = models.checks.objects.filter(owner=self.request.user.username)
        return context


class help(FormView):
    template_name = 'pages/help.html'
    success_url = '/help'
    form_class = forms.help_form

