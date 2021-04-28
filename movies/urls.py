from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.MovieCreateView.as_view(), name='movie_create'),
    path('list/', views.MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/detail/', views.MovieRetrieveView.as_view(), name='movie_retrieve'),
    path('movie/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie_delete'),
    path('movie/<int:pk>/update/', views.MovieUpdateView.as_view(), name='movie_update'),

    path('list-create/', views.MovieListCreateView.as_view(), name='movie_list_create'),
    path('movie/<int:pk>/retrieve-update/', views.MovieRetrieveUpdateView.as_view(), name='movie_retrieve_update'),
    path('movie/<int:pk>/retrieve-destroy/', views.MovieRetrieveDestroyView.as_view(), name='movie_retrieve_destroy'),
    path('movie/<int:pk>/retrieve-update-destroy/', views.MovieRetrieveUpdateDestroyView.as_view(), name='movie_retrieve_update_destroy')
]
