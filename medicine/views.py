from django.shortcuts import render, redirect
from django.contrib.auth import login
# from .forms import UserRegistrationForm
# from .models import UserProfile

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the medicine index.")

# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user_profile = UserProfile(user=user, user_type=form.cleaned_data['user_type'])
#             user_profile.save()
#             login(request, user)  # Автоматически войти после регистрации
#             return redirect('/')  # Перенаправление на главную страницу
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'registration.html', {'form': form})