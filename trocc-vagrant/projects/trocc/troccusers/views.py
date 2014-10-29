from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import UserCreationForm, TroccUserForm
from django.http.response import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render_to_response, render, redirect, resolve_url
from django.template import RequestContext
from .models import TroccUser
from . import log
from django.views.generic import TemplateView, FormView, DetailView, CreateView
# Create your views here.

class LoginUserView(TemplateView):
    template_name = "troccusers/login.html"

    def __init__(self, *args, **kwargs):
        self.error = False
        super(LoginUserView, self).__init__(*args, **kwargs)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect("/my_products")
        else:
            self.error = True

        return render(
        request = self.request,
        template_name = self.template_name,
        dictionary = {"error" : self.error}
        )

class SignUpView(FormView):
    template_name = "troccusers/signup.html"
    form_class = UserCreationForm

    def __init__(self, *args, **kwargs):
        self.registered = False;
        super(SignUpView, self).__init__(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        self.registered = True
        #return redirect to the same page with registered variable passed to the context
        return render(
            self.request,
            template_name = "troccusers/signup.html",
            dictionary = {"registered" : self.registered}
            )

    def form_invalid(self, form):
        return super(SignUpView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context =  super(SignUpView, self).get_context_data(**kwargs)
        context['registered'] = self.registered
        return context

def index(request):
    return render(
        request = request,
        template_name = "troccusers/main.html",
        dictionary = {}
    )

@login_required()
def logout_user(request):
    logout(request)
    return render(
        request = request,
        template_name = "troccusers/main.html",
        dictionary = {}
    )