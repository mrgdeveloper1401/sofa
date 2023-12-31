from django.contrib import admin
from .models import Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('product','sku', 'buy_price','sale_price', 'num_stock', 'is_active')
    list_editable = ('is_active', )
    search_fields = ('product', 'product','sku', 'buy_price')
    list_per_page = 20
    list_filter = ('is_active', 'create_at', 'update_at')