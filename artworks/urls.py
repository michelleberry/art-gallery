from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artworks/about_me', views.about_me, name='about_me'),
    path('<int:pk>/', views.collection_index, name='collection_index'),
    path('<int:collection_id>/<int:art_id>/', views.art_details, name='art_details'),
]
