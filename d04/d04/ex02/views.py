from django.shortcuts import render
from .forms import Myform
from django.conf import settings
from datetime import datetime


def make_log(form):
    with open(settings.LOGFILE, 'a') as logs_file:
        logs_file.write(f"{datetime.now()} {form.cleaned_data['content']}\n")


def get_logs():
    logs = []
    with open(settings.LOGFILE) as logs_file:
        for log in logs_file:
            logs.append(log)
    return logs


def add_form(request):
    if request.method == 'POST':
        form = Myform(request.POST)
        if form.is_valid():
            make_log(form)
    with open(settings.LOGFILE, 'a') as for_create:
        pass
    form = Myform()
    logs = get_logs()
    context = {
        'title': 'Ex02: Form',
        'form': form,
        'logs': logs,
    }
    return render(request, 'ex02/my_form.html', context=context)
