from django.contrib import admin
from .models import Product, Rating, UserCart, FavouriteProduct


admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(UserCart)
admin.site.register(FavouriteProduct)