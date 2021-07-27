from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from .forms import *
import  subprocess

import sys
def home_page(request):
    return render(request, 'home_page/home_page.html')



"""Регистрация"""
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('home_page')




# def summ_client (request):
#     if request.method == 'POST':
#         form = SummClientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home_page')
#         else:
#
#
#             form = SummClientForm()
#             data = {
#                 'form': form,
#
#
#             }
#
#         return render(request, "bot/bot.html", data)



class ContactFormView(FormView):
    template_name = 'bot/bot.html'
    form_class = SummClientForm
    success_url = reverse_lazy('bot')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        form.save()
        a = subprocess.Popen([sys.executable, 'API.py'])
        code = a.wait()
        print(code)
        return super().form_valid(form)
    def get_context_data(self, *, object_list=None, **kwargs):
        context_1 = super().get_context_data(**kwargs)
        context_1['menu'] = '1'
        context = super().get_context_data(**kwargs)
        return context_1
