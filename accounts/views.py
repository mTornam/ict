from django.shortcuts import render, redirect
from .forms import CreateStaffForm
from django.contrib.auth.forms import PasswordResetForm
# Create your views here.
def signUp(request):
    form = CreateStaffForm(request.POST or None)
    context = {
        'form': form
    }
    
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        user.set_password('Welcome@124')  # Set a default password
        user.is_active = True
        user.save()

        reset_form = PasswordResetForm({'email': user.email})
        if reset_form.is_valid():
            reset_form.save(
                request=request,
                use_https=request.is_secure(),
            )
        return redirect('service_tracker:index') 
    
    return render(request, 'accounts/sign-up.html', context)