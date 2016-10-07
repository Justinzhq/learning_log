from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def logout_view(request):
    """log out"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(requset):
    """register"""
    if requset.method != 'POST':
        # empty
        form = UserCreationForm()
    else:
        # form
        form = UserCreationForm(data=requset.POST)

        if form.is_valid():
            new_user = form.save()
            # re
            authenticated_user = authenticate(username=new_user.username,
                                              password=requset.POST['password1'])
            login(requset, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(requset, 'users/register.html', context)
