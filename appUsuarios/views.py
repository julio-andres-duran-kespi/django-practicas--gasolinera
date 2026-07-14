from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import customUserCreationForm
# Create your views here.
User = get_user_model()
def home(request):
    return render(request, 'appUsuarios/home.html')

def login(request):
    return render(request, 'appUsuarios/login.html')

class RegistroView(CreateView):
    model = User
    form_class = customUserCreationForm
    template_name = 'appUsuarios/registro.html'
    success_url = reverse_lazy('appUsuarios:login')
    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. Comuniquese con el Admin.')
        return super().form_valid(form)