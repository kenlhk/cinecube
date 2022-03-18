
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import User


# Create your views here.


# Landing Page
def login(request):
    # Record the address of the previous page
    url = request.META.get('HTTP_REFERER', '/   ')
    print(url)
    request.session['preUrl'] = url
    if request.method == 'GET':
        return render(request, 'movies/login.html')
    else:
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')

        # Check if a user exists
        try:
            u = User.objects.get(username=nickname)
        except User.DoesNotExist as e:
            return redirect('user:login')

        # If present, verify that the password is correct
        if password != u.password:
            return redirect('user:login')

        # Login successful
        response = redirect('movies:movie_list')
        token = make_password(nickname)
        u.token = token
        u.save()
        response.set_cookie('userToken', token)
        request.session['username'] = u.username
        response.set_cookie('usernameKey', 'username')

        return response


# Registration Page
def register(request):
    if request.method == 'GET':
        return render(request, 'movies/register.html')
    else:
        # In case of ajax requests
        if request.is_ajax():
            # Verify that the account exists
            nickname = request.POST.get('nickname')
            try:
                user = User.objects.get(username=nickname)
                # Indicates that the account has been used
                return JsonResponse({'data':'1'})
            except User.DoesNotExist as e:
                # Determine if a email is available
                email = request.POST.get('email')
                try:
                    email_user = User.objects.get(email=email)
                    # Indicates that the email is occupied
                    return JsonResponse({'data':'2'})
                except User.DoesNotExist as e:
                    # Email available
                    return JsonResponse({'data':'3'})
                # Indicates the account can use
                return JsonResponse({'data':'0'})
        # Verify that the account exists


        # If all information is verified, the registered user
        else:
            nickname = request.POST.get('nickname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            # try:
            #     User.objects.get(username=nickname)
            #     User.objects.get(email=email)
            # except User.DoesNotExist as e:
            #     return redirect('user:register')

            # User token
            userToken = make_password(nickname)

            # create user
            password=make_password(password)
            user = User.createuser(username=nickname, password=password, email=email, token=userToken)
            user.save()

            # Registering successfully requires a state hold, a session, and a default login.
            request.session['username'] = nickname
            response = redirect('movies:index')
            response.set_cookie('usernameKey', 'username')
            response.set_cookie('userToken', userToken)

            return response


# 退出页
from django.contrib.auth import logout
def quit(request):
    logout(request)
    return redirect('movies:index')
