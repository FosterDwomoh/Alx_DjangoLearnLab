from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'forms': form})

    @login_required
    def profile(request):
        if request.method == 'POST':
            user = request.userform = CustomUserCreationForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = CustomUserCreationForm(instance=request.user)
            return render(request, 'registration/profile.html', {'form': form})