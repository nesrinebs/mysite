from django.shortcuts import render

# Create your views here.
from auth.forms.userregisterform import UserRegistrationForm
from auth.forms.usereditform import UserEditForm
from auth.forms.userloginform import UserLoginForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,  redirect, get_object_or_404
from django.contrib.auth.models import User



def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(
                request, 'Your are Registered !! please login to continue ')
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

       

    # status = request.session.get('status', '')

    # if redirect:
    #     response = HttpResponseRedirect(redirect)
    #     if status:
    #         response.set_cookie('status_type', status['type'])
    #         response.set_cookie('status_msg', status['msg'])
    # else:
    #     data = {
    #         'form': form,
    #         'status': status
    #     }
    #     return render(request, 'register.html', data)


def home_view(request):
    return render(request, 'home.html')


@login_required
def profiles_view(request):
    users = User.objects.all()
    return render(request, 'profiles.html', {'users': users})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.info(request, 'Your logged in  successfully!')
                return redirect('profiles')
            else:
                messages.info(request, 'Please enter correct details ')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Invalid Credentials !!!')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')

    """ redirect = None
   

    login_form = UserLoginForm()
    
    if request.user.is_authenticated():
        redirect = reverse('edit')
    else:
        if request.method == 'POST':
            login_form = UserLoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.info(request, 'Your logged in  successfully!')
                    if 'next' in request.GET:
                        redirect = request.GET['next']
                    return redirect('edit')
                else:
                    messages.info(request, 'Please enter correct details ')
                    return render(request, 'login.html')
            else:
                messages.info(request, 'Invalid Credentials !!!')
                return render(request, 'login.html')

        else:
            return render(request, 'login.html') """


def edit_view(request, id=None):

    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(
                request, 'Email updated successfully logged in  successfully!')
            return HttpResponseRedirect(request.path_info)

        else:
            return render(request, 'edit.html', {'form': form})
    else:
        form = UserEditForm(instance=user)
        return render(request, 'edit.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You logged out !!!! please login to continue')
    return redirect('/login')
