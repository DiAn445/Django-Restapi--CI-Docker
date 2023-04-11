from django.urls import path, include
from Cat_kinds.views import *
from django.views.generic.base import RedirectView
from .views import add_to_cart, remove_from_cart, cart, CatsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cat_kinds', CatsViewSet)

urlpatterns = [
    path('', index, name='home'),
    path('sign_up/', RegisterUser.as_view(), name='sign_up'),
    path('sign_in/', LogInUser.as_view(), name='sign_in'),
    path('log_out/', logout_user, name='log_out'),
    path('Anya/', about, name='Anya'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    path('cart/', cart, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls))
]