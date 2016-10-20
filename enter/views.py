from django.shortcuts import render
from enter.models import Product, Store, User
from django.template import RequestContext
from enter.forms import ProductForm, StoreForm, UserForm
from django.shortcuts import render_to_response


def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
    else:
        form = ProductForm()
    return render(request, 'flask/add_product.html', {'form': form})


def add_store(request):
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
    else:
        form = StoreForm()
    return render(request, 'flask/add_store.html', {'form': form})


def product(request):
    context_dict = {}
    context = RequestContext(request)
    product_list = Product.objects.all()
    for product in product_list:
        context_dict = {'products': product_list}
    return render_to_response('flask/available_product.html', context_dict, context)


def store(request):
    context_dict = {}
    context = RequestContext(request)
    store_list = Store.objects.all()
    for store in store_list:
        context_dict = {'stores': store_list}
    return render_to_response('flask/available_store.html', context_dict, context)


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
    else:
        form = UserForm()
    return render(request, 'flask/register.html', {'form': form})