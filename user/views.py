from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    return render(request, 'user/profile.html')


def dashboard(request):
    return render(request, 'admin/dashboard.html')



def create_profile():
    pass


def read_profile():
    pass


def update_profile():
    pass


def delete_profile():
    pass

def admin():
    pass
