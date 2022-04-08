from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    #path('<int:pk>/', views.single_post_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    #path('', views.index),
    path('category/<str:slug>/', views.show_category_posts)
]