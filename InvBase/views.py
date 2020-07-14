from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from django import template

register = template.Library()

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "index.html"
    success_url = "/main/"

    def is_group(user, group_name):
        try:
            group =  Group.objects.get(name=group_name)
            return group in user.groups.all()
        except Group.DoesNotExist:
            return False

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")