from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('play/', views.play_page, name='play_page'),
    path('team/', views.team_page, name='team_page'),
    path('gallery/', views.gallery_page, name='gallery_page'),
    path('tickets/', views.tickets_page, name='tickets_page'),
    path('new/', views.ticket_create, name='ticket_form'),
    path('delete/<int:pk>', views.ticket_delete, name='ticket_delete'),
    path('edit/<int:pk>', views.ticket_update, name='ticket_edit'),
    path('playinfo/', views.playinfo_page, name='play-info-detail'),
    path('author/<int:pk>', views.author_page.as_view(), name='author-detail'),
    path('author/', views.author_page, name='authors-detail'),
    path('actor/<int:pk>', views.actor_detail.as_view(), name='actor-detail'),
    path('reviews/', views.reviews_page, name='reviews_page'),
    path('review/', views.review_create, name='review_form'),
    path('review/<int:pk>', views.review_page.as_view(), name='review-detail'),
]
