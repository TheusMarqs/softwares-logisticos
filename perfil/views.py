from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

@login_required()
def home(request):
    return render(request, 'home.html')

@login_required()
def meu_perfil(request):
    return render(request,'meu_perfil.html')