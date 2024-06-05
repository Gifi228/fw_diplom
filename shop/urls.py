from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', category_page_view, name='category'),
    path('article/<int:article_id>/', article_detail_view, name="article_detail"),

    path('add_article/', add_article, name='add_article'),

    path('register/', register_user_view, name='register'),
    path('login/', login_user_view, name='login'),
    path('logout/', logout_user_view, name='logout'),

    path('update_article/<int:article_id>/', update_article_view, name='update_article'),
    path('delete_article/<int:article_id>/', article_delete, name='delete_article'),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('edit_user/<int:user_id>/', update_profile_view, name='update_profile'),
    path('save_comment/<int:article_id>/', save_comment, name="save_comment"),
    path('search/', search_view, name='search'),

    path('basket_add/<int:article_id>/', basket_add, name='basket_add'),
    path('remove_from_basket/<int:basket_id>/', basket_remove, name='remove_from_basket'),
    path('my_basket/', basket_show, name='my_basket'),

    path('article/<int:article_id>/add_to_favorites/', add_to_favorites, name='add_to_favorites'),
    path('article/<int:article_id>/remove_from_favorites/', remove_from_favorites, name='remove_from_favorites'),
    path('favorites/', favorite_list, name='favorite_list'),
]
