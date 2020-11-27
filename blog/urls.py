from django.urls import path
from .views import HomeView, ArticleDetailView #, AddPostView, UpdatePostView, DeletePostView #category_list ,  #CatListView #post_create, post_update ,
from .import views

app_name = 'blog'

urlpatterns = [
    #path('', views.post_list,name='post-list'),
    #path('<slug:category_slug>', views.home,name='post_by_category'),
    #path('category/<slug:category_slug>/>', views.category_list, name='post_by_category'),
    #path('<int:pk>/', views.article_detail, name='article-detail'),
    path('', HomeView.as_view(),name='post-list'),
    #path('category/<slug:slug>/', views.category_list, name='category'),
    #path('category/<slug:slug>/',views.category,name='category'),
    path('article/<int:pk>', ArticleDetailView.as_view(),name='article-detail'),
    path('newsletter/', views.newsletter_signup,name='newsletter'),
    #path('category/<category>', CatListView.as_view(),name='category'),
    #path('create/', AddPostView.as_view(),name='post-create'),
    #path('article/<int:pk>/edit/', UpdatePostView.as_view(),name='update-post'),
    #path('article/<int:pk>/remove/', DeletePostView.as_view(),name='delete-post'),
    path('create/', views.post_create, name='post-create'),
    path('article/<int:pk>/update/', views.post_update, name='post-update'),
    path('article/<int:pk>/delete/', views.post_delete, name='post-delete'),
]