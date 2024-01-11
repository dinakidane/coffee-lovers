from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse_lazy

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return reverse_lazy('index') 