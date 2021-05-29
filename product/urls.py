from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageProductListView.as_view(), name='index'),
    path('category/<str:product_category>/', views.ProductCategoryListView.as_view(), name="product_category"),
    path('update_cart/', views.update_cart),
    path('cart_total/', views.get_user_cart_total),
    path('product/<str:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/<str:pk>/all-reviews', views.ProductReviewsView.as_view(), name='product_reviews'),
    path('update_favourites/', views.update_favourites),
    path('cart/', views.CartPage.as_view(), name='cart'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
]