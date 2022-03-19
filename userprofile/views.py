from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from userprofile.forms import UserForm, UserProfileForm


# Create your views here.

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get("password")
#
#         user = authenticate(username=username, password=password)
#
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return redirect(reverse('movies:index'))
#             else:
#                 return HttpResponse("Your account is disabled.")
#         else:
#             print(f"Invalid login details: {username}, {password}")
#             return HttpResponse("Invalid login details supplied")
#
#     else:
#         return render(request, 'userprofile/login.html')
#
#
# def register(request):
#     registered = False
#
#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#         profile_form = UserProfileForm(request.POST)
#
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#
#             user.set_password(user.password)
#             user.save()
#
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()
#
#             registered = True
#
#         else:
#             print(user_form.errors, profile_form.errors)
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileForm()
#
#     return render(request,
#                   'userprofile/register.html',
#                   context={'user_form': user_form,
#                            'profile_form': profile_form,
#                            'registered': registered})
#
#
# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect(reverse('movies:index'))
