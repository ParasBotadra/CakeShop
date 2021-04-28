from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('user-registration/', views.UserRegistration.as_view(), name='user_registration'),
    path('post-collection/', views.PostCollection.as_view(), name='post_collection'),
    url(r'^post-element/(?P<pk>[0-9]+)$', views.PostElement.as_view(), name='post_element'),
]
