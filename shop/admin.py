# from django.contrib.admin import AdminSite
# from django.contrib import admin

# # Register your models here.
# from .models import Product
# from .models import checkout
# from .models import Form
# from .models import Coupon
# from .models import Brand
# from .models import Orders

# admin.site.register(Product)
# admin.site.register(checkout)
# admin.site.register(Form)
# admin.site.register(Coupon)
# admin.site.register(Brand)
# admin.site.register(Orders)

# class ShopAdminSite(AdminSite):
#     site_header = "Shop Admin"
#     site_title = "Shop Admin Portal"
#     index_title = "Welcome to the Shop Admin"


# shop_admin_site = ShopAdminSite(name='shop_admin')

# @admin.register(Product, site=shop_admin_site)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'content')

from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Product, checkout, Form, Coupon, Brand, Orders

# Register models with the default admin
admin.site.register(Product)
admin.site.register(checkout)
admin.site.register(Form)
admin.site.register(Coupon)
admin.site.register(Brand)
admin.site.register(Orders)

# Custom admin site for shop
class ShopAdminSite(AdminSite):
    site_header = "Shop Admin"
    site_title = "Shop Admin Portal"
    index_title = "Welcome to the Shop Admin"

shop_admin_site = ShopAdminSite(name='shop_admin')

# Register Product model with custom admin site
@admin.register(Product, site=shop_admin_site)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price')  # Replace with real fields from your Product model
    list_filter = ("product_name", "price","category")

    def category(self, obj):
        return obj.benevolence_factor > 75


@admin.register(Orders, site=shop_admin_site)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'city','state')

