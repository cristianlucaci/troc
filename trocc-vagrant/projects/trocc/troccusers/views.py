from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import UserCreationForm, TroccUserForm, TradeForProductForm, TradeInProductForm, CategoryForm
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from .models import TroccUser, TradeForProduct, TradeInProduct
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

class MyProductsView(DetailView):

    def __init__(self):
        self.product_form = TradeInProductForm()
        self.category_form = CategoryForm()
        self.products = None
        super(MyProductsView, self).__init__()

    def get(self, request, *args, **kwargs):
        query_dict = {"user_id": self.request.user.id}
        self.products = TradeInProduct.objects.filter(**query_dict).order_by("name")

        return render(
                    request = request,
                    template_name = "troccusers/myProducts.html",
                    dictionary = {"product_form":self.product_form,
                                  "products": self.products,
                                  "category_form" : self.category_form}
                )

    def post(self, request):
        #Even though it doesn't hit the db there must be a better way
        query_dict = {"user_id": self.request.user.id}
        self.products = TradeInProduct.objects.filter(**query_dict).order_by("name")

        self.product_form = TradeInProductForm(request.POST)
        self.category_form = CategoryForm(request.POST)
        if self.category_form.is_valid():
            self.category_form.save()
        else:
            print self.category_form.errors

        if self.product_form.is_valid():
            self.product_form.save(user = request.user)
        else:
            print self.product_form.errors

        return render(
                request = request,
                template_name = "troccusers/myProducts.html",
                dictionary = {"product_form": self.product_form,
                              "products": self.products,
                              "category_form" : self.category_form}
                )

@login_required()
def logout_user(request):
    logout(request)
    return render(
        request = request,
        template_name = "troccusers/main.html",
        dictionary = {}
    )