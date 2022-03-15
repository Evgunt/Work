from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, PasswordChangeView
from datetime import datetime

from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, TemplateView, UpdateView
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
                if models.AdvUser.objects.filter(Q(username=username) | Q(email=username)).exists():
                    AdvUser = models.AdvUser.objects.get(Q(username=username) | Q(email=username))
                    success = authenticate(username=AdvUser.username, password=password)
                    if success is None:
                        context['password'] = 'Неверный пароль'
                    else:
                        login(request, success)
                        return redirect('/keys')
                else:
                    context['password'] = 'Неверный пароль'
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

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/keys')
        else:
            return render(request, 'user/createUser.html')


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

    def post(self, request, *args, **kwargs):
        pk = request.POST['pk']
        name = request.POST['name']
        if name != '':
            keysBd = models.keys.objects.get(pk=pk)
            keysBd.name = name
            keysBd.save()
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)


class req(LoginRequiredMixin, TemplateView):
    template_name = 'pages/req.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_req'] = models.requisites.objects.filter(owner=self.request.user.username)
        return context


class requisites_add(LoginRequiredMixin, CreateView):
    template_name = 'pages/req_add.html'
    success_url = '/requisites_add'
    form_class = forms.add_req_form
    login_url = '/'

    def post(self, request, *args, **kwargs):
        context = {'display': 'none'}
        form = forms.add_req_form(request.POST)
        if form.is_valid():
            context['display'] = 'block'
            instance = form.save(commit=False)
            instance.owner = self.request.user
            if models.requisites.objects.filter(owner=request.user.username).exists():
                instance.type = 'Дополнительный'
            else:
                instance.type = 'Основной'
            instance.save()
        return render(self.request, 'pages/req_add.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['display'] = 'none'
        return context


class ChangeRequisites(LoginRequiredMixin, UpdateView):
    model = models.requisites
    template_name = 'pages/req_edit.html'
    form_class = forms.add_req_form
    success_url = '/requisites'
    login_url = '/'
    pk_url_kwarg = id

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        return get_object_or_404(queryset, pk=pk, owner=self.request.user.username)


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
    if request.user.is_authenticated:
        return redirect('/keys')
    else:
        context = {'display': 'none'}
        if request.method == "POST":
            username = request.POST['username']
            if models.AdvUser.objects.filter(Q(username=username) | Q(email=username)).exists():
                user = models.AdvUser.objects.get(Q(username=username) | Q(email=username))
                utilities.send_password_notification(user)
                context['mail'] = "Проверьте почту"
                context['display'] = 'block'
            else:
                context['errors'] = "Введен неверный логин"
        return render(request, 'user/password_email_form.html', context)


def password_email(request, sign):
    username = utilities.signer.unsign(sign)
    user = get_object_or_404(models.AdvUser, username=username)
    password = utilities.generate_password()
    user.set_password(password)
    user.save()
    context = {'user': username, 'password': password}
    return render(request, 'user/password_change_email.html', context)


class checks(LoginRequiredMixin, CreateView):
    model = models.checks
    form_class = forms.UploadFileForm
    template_name = 'pages/checks.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_checks'] = models.checks.objects.filter(owner=self.request.user.username)
        return context

    def post(self, request, *args, **kwargs):
        context = {'success': 0, 'list_checks': models.checks.objects.filter(owner=request.user.username)}
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            if models.checks.objects.filter(pk=request.POST['pk'], owner=request.user.username).exists():
                check = models.checks.objects.get(pk=request.POST['pk'], owner=request.user.username)
                check.pay = request.FILES['pay']
                check.save()
            context['success'] = 1

        return render(request, 'pages/checks.html', context)


class Help(LoginRequiredMixin, CreateView):
    template_name = 'pages/help.html'
    success_url = '/help'
    form_class = forms.help_form
    login_url = '/'

    def post(self, request, *args, **kwargs):
        context = {'display': 'none'}
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = self.request.FILES.getlist('inv')
        if form.is_valid():
            id = form.save().pk
            helpMessage = models.helpMessage.objects.get(pk=id)
            if files:
                for f in files:
                    fl = models.Files_helps(helps=helpMessage, file=f)
                    fl.save()
            context['display'] = 'block'
        self.form_valid(form)
        return render(self.request, 'pages/help.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['display'] = 'none'
        return context


class profile(LoginRequiredMixin, TemplateView):
    template_name = 'pages/profile.html'
    login_url = '/'


class changePass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user/changePass.html'
    success_url = '/profile'
    login_url = '/'


class ChangeUser(LoginRequiredMixin, UpdateView):
    model = models.AdvUser
    template_name = 'user/user_edit.html'
    form_class = forms.edit_user_form
    success_url = '/profile'
    login_url = '/'
    pk_url_kwarg = id

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        return get_object_or_404(queryset, pk=pk, username=self.request.user.username)
