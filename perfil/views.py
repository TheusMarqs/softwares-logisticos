from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

@login_required()
def meu_perfil(request):
    return render(request,'meu_perfil.html')