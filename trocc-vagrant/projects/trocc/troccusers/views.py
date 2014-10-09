from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import UserCreationForm, TroccUserForm, TradeForProductForm, TradeInProductForm, CategoryForm
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from .models import TroccUser, TradeForProduct, TradeInProduct
from . import log
from django.views.generic import ListView, FormView
# Create your views here.

class LoginUser(FormView):
    template_name = "troccusers/login.html"
    error = False
    form_class = TroccUserForm
    success_url = "/my_products"

    def get(self, request, *args, **kwargs):
        return HttpResponse()

    def form_valid(self, form):
        username = form.instance.username
        password = form.instance.password

        user = authenticate(username=username, password=password)

        if user is None or user.is_active == False:
            error = True
        return super(LoginUser, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context =  super(LoginUser, self).get_context_data(**kwargs)
        context['error'] = self.error
        return context

# def login_user(request):
#     error = False
#
#     if request.POST:
#         username = request.POST["username"]
#         password = request.POST["password"]
#
#         user = authenticate(username=username, password=password)
#
#         if user is not None and user.is_active:
#             login(request, user)
#             return HttpResponseRedirect("/my_products")
#         else:
#             error = True
#
#     return render(
#         request = request,
#         template_name = "troccusers/login.html",
#         dictionary = {"error" : error}
#     )

def sign_up(request):
    registered = False
    context = RequestContext(request)
    if request.POST:
        user_form = UserCreationForm(data = request.POST)
        if user_form.is_valid():
            user_form.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserCreationForm()

    return render_to_response(
            'troccusers/signup.html',
            {'user_form': user_form, 'registered': registered},
            context)


def index(request):
    return render(
        request = request,
        template_name = "troccusers/main.html",
        dictionary = {}
    )

@login_required()
def my_products(request):
    query_dict = {"user_id": request.user.id}
    products = TradeInProduct.objects.filter(**query_dict).order_by("name")

    if request.POST:
        product_form = TradeInProductForm(request.POST)
        category_form = CategoryForm(request.POST)
        if "add_category" in request.POST:
            if category_form.is_valid():
                category_form.save()
            else:
                print category_form.errors
        elif "add_product" in request.POST:
            if product_form.is_valid():
                product = product_form.save(user = request.user)
                request.user.products.add(product)
                request.user.save()
            else:
                print product_form.errors
    else:
        product_form = TradeInProductForm()
        category_form = CategoryForm()

    return render_to_response(
            "troccusers/myProducts.html",
            {
                "username": request.user.username,
                "products": products,
                "product_form": product_form,
                "category_form": category_form,

            },
            context_instance=RequestContext(request),
        )


@login_required()
def logout_user(request):
    logout(request)
    return render(
        request = request,
        template_name = "troccusers/main.html",
        dictionary = {}
    )