from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start, name='start'),
    path('', views.home, name='home'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('routine/', views.routine, name='routine'),
    path('search/', views.search, name='search'),
    path('wishlist/<int:user_id>', views.wishlist, name='wishlist'),
    path('product/', views.product, name='product'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('add_to_wishlist/<int:user_id>/<int:product_id>', views.add_to_wishlist, name='add_to_wishlist'),
    path('add_to_wishlist_routine/<int:user_id>/<int:product_id>', views.add_to_wishlist_routine, name='add_to_wishlist_routine'),
    path('del_wishlist/<int:product_id>', views.del_wishlist, name='del_wishlist'),
]