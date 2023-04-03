from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView
from .forms import RegisterUserForm, LogInUserForm
from .utils import *
from .models import Cart


@csrf_protect
def index(request):
    if 'american' in request.POST:
        plus_like(american)
    elif 'manul' in request.POST:
        plus_like(manul)
    elif 'abyss' in request.POST:
        plus_like(abyss)
    elif 'siamese' in request.POST:
        plus_like(siamese)
    elif 'bengal' in request.POST:
        plus_like(bengal)
    elif 'british' in request.POST:
        plus_like(british)

    context = {'Title': 'Cats', 'american': american.likes, 'british': british.likes, 'bengal': bengal.likes,
               'siamese': siamese.likes,
               'manul': manul.likes, 'abyss': abyss.likes}

    return render(request, 'cats/index.html', context=context)


@login_required(login_url='/admin')
def about(request):
    return render(request, 'cats/about.html', {'Title': 'Anya'})


def show_post(request, post_id):
    return HttpResponse(f"card num: {post_id}")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'cats/sign_up.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LogInUser(LoginView):
    form_class = LogInUserForm
    template_name = 'cats/sign_in.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('sign_in')


def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cats/cart.html', {'cart': cart})


def add_to_cart(request, product_id):
    product = CatKinds.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    return redirect('cart')


def remove_from_cart(request, product_id):
    product = CatKinds.objects.get(id=product_id)
    cart = Cart.objects.get(user=request.user)
    cart.products.remove(product)
    return redirect('cart')


