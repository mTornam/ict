from django.views import generic
from .models import Staff
from .forms import CreateStaffForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

# Create your views here.
class CreateStaffView(LoginRequiredMixin, generic.CreateView):
    model = Staff
    form_class = CreateStaffForm
    template_name = 'accounts/sign-up.html'
    success_url = reverse_lazy('service_tracker:index')

    def dispatch(self, request, *args, **kwargs):
        # Only allow superusers to access this view
        if not request.user.is_superuser:
            return HttpResponseForbidden("You do not have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)

class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('service_tracker:index')

    def form_valid(self, form):
        # Get cleaned data from form
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # Authenticate the user
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(self.request, user)
            return super().form_valid(form)
        else:         
            form.add_error(None, 'Invalid username or password')
            return self.form_invalid(form)


class ForcePasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'accounts/password-change.html'
    success_url = reverse_lazy('service_tracker:index')

    def form_valid(self, form):
        # Remove the force_password_change flag after a successful password change
        user = self.request.user
        user.force_password_change = False
        user.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

