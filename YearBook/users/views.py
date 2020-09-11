from django.shortcuts import render,redirect                    # redirect fo rredirecting the pages 
from django.contrib.auth.forms import UserCreationForm          # Not using this import 
from django.contrib import messages                             # to print one time message just like toast in Android
from .forms import UserRegistrationForm,UserUpdateForm, ProfileUpdateForm                        # We have implemented our own Registration form by extending the default UserCreationForm
from django.contrib.auth.decorators import login_required 




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()                                                                     # saves the data from the form
            username = form.cleaned_data.get('username')                                    # retrives the data of username
            messages.success(request, f'Account has been created { username }! ')           # sends messages as toaster
            return redirect('login')                                                        # redirecting the page to Blog-home
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', { 'form': form } )


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            messages.success(request, f'Account has been updated ! ')           # sends messages as toaster
            return redirect('profile')    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

