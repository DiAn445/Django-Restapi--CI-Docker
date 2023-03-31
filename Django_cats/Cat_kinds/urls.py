from django.urls import path
from Cat_kinds.views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', index, name='home'),
    path('sign_up/', RegisterUser.as_view(), name='sign_up'),
    path('sign_in/', LogInUser.as_view(), name='sign_in'),
    path('log_out/', logout_user, name='log_out'),
    path('Anya/', about, name='Anya'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True))
]