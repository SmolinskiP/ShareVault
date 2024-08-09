from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import File
from .forms import LoginForm, FileUploadForm
from django.contrib.auth import login, authenticate, logout
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import JsonResponse
import os
import logging
from django.utils import timezone
import datetime
logger = logging.getLogger(__name__)


def redirect_to_login(request):
    if request.user.is_authenticated:
        return redirect('file_list')
    else:
        return redirect('login')

@login_required
def file_list(request):
    files = File.objects.filter(user=request.user)
    context = {
        'files': files,
        'title': _("Twoje Pliki")
    }
    return render(request, 'filemanager/file_list.html', {'files': files})

@login_required
def test_email(request):
    user = request.user
    test_file = File.objects.filter(user=user).first()
    if test_file:
        send_expiration_email(user, test_file)
    return HttpResponse('Test email sent.')

def send_expiration_email(user, file):
    subject = 'Przypomnienie o wygasnieciu pliku'
    message = f'Plik "{file.filename}" wygasnie {file.expiration_date}. Pobierz go zanim to nastapi.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, email_from, recipient_list)

@login_required
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_list')
    else:
        form = UserCreationForm()
    return render(request, 'filemanager/create_user.html', {'form': form})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'filemanager/user_list.html', {'users': users})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('file_list')
    else:
        form = LoginForm()
    return render(request, 'filemanager/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def file_list(request):
    files = File.objects.filter(user=request.user)
    return render(request, 'filemanager/file_list.html', {'files': files})

@login_required
def download_file(request, file_id):
    file_instance = get_object_or_404(File, id=file_id, user=request.user)
    file_path = file_instance.file.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def error_404(request):
        data = {}
        return render(request,'404.html', data)

def error_500(request):
        data = {}
        return render(request,'500.html', data)
