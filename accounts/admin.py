from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from accounts.models import Account
from accounts.forms import AccountChangeForm, AccountCreationForm

class AccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = Account
    list_display = ['email', 'username', 'first_name', 'last_name', 'location']

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('location', 'profile_photo',)}),
    )


admin.site.register(Account, AccountAdmin)