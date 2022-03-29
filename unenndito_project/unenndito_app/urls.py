from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    
    path('postlist/', views.post_list, name='postlist'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),

    path('error404/', views.error404, name='error404'),
    path('error500/', views.error500, name='error500'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('faq/', views.faq, name='faq'),
]










