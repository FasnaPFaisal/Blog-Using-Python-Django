
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-me/', views.about_me, name='about-me'),
    path('recent-posts/', views.recent_posts, name='recent-posts'),
    path('add-posts/',views.add_post,name='add-post'),
    path('reading/<id>', views.reading, name = "reading"),
    path('edit/<id>', views.edit, name='edit'),
    path('delete/<id>', views.delete, name='delete'),
]
