from .forms import CategoryForm, TradeForProductForm, TradeInProductForm
from utils.mixins import LoginRequiredMixin
from models import TradeForProduct, TradeInProduct
from django.shortcuts import render


from django.views.generic import TemplateView, FormView, DetailView

# Create your views here.
class MyProductsView(LoginRequiredMixin, DetailView):


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
                    template_name = "troccproducts/myProducts.html",
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
                template_name = "troccproducts/myProducts.html",
                dictionary = {"product_form": self.product_form,
                              "products": self.products,
                              "category_form" : self.category_form}
                )

myProducts = MyProductsView.as_view()