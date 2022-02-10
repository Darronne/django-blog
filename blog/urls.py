from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:post_url>', views.post, name='post'),
    path('region/<slug:region_url>', views.region, name='region'),
    path('part/<slug:part_url>', views.part, name='part'),
]