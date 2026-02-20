from django.shortcuts import redirect
from django.urls import reverse_lazy
class ForcePasswordChangeMiddleware:
    """
    Middleware to force users to change their password on first login.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_paths = [
            reverse_lazy('accounts:force-password-change'),
            reverse_lazy('accounts:logout'),
        ]
        
        if request.user.is_authenticated and request.user.force_password_change:
            # Redirect to the password change page
            if request.path not in allowed_paths:
                return redirect('accounts:force-password-change')

        response = self.get_response(request)
        return response