from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cont creat! Acum va puteti loga!')
            return redirect('retete-acasa')
    else:
        form = UserRegisterForm()
    return render(request, 'utilizatori/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'utilizatori/profil.html')