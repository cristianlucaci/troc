__author__ = 'marianlungu'
from allauth.account.adapter import DefaultAccountAdapter
from .models import TroccUser
from django.core.urlresolvers import reverse_lazy, reverse


class AccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        return reverse('troccproducts.products')

    def new_user(self, request):
        user = TroccUser()
        return user

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        if 'password1' in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        super(AccountAdapter, self).populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user

    def confirm_email(self, request, email_address):
        super(AccountAdapter, self).confirm_email(request, email_address)
