from django.urls import path
from Cat_kinds.views import *

urlpatterns = [
    path('', index, name='home'),
    path('Anya/', about, name='Anya'),
    path('post/<int:post_id>/', show_post, name='post')
]