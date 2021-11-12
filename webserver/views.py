from django.http import HttpResponse
from django.shortcuts import render

from .forms import Login
from .rawsql import raw


def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if (form.is_valid() and raw(form.cleaned_data['username'], form.cleaned_data['password']) != None):
            return HttpResponse('Successful login!')
        else:
            return HttpResponse('Error!')
    else:
        form = Login()

    return render(request, './login.html', {'form': form})
