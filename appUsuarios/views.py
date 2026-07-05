from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'appUsuarios/login.html')

def register_view(request):
    return render(request, 'appUsuarios/registro.html')