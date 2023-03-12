from django.contrib import admin
from.models import Product,Variations
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display =  ('product_name','price','stock','category','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}

class VariationsAdmin(admin.ModelAdmin):
    list_display=('product','variation_category','variation_value','is_active','created_date',)
    list_editable=('is_active',)
    list_filter=('product','variation_category','variation_value',)

admin.site.register(Variations,VariationsAdmin)
admin.site.register(Product)