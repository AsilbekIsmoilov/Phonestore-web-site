from django.contrib import admin
from django.utils.safestring import mark_safe

from store.models import Category, Product, Gallery, Like, Order, OrderProduct


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title','get_count','image']
    prepopulated_fields = {'slug':('title',)}


    def get_count(self,obj):
        if obj.products:
            return str(len(obj.products.all()))
        else:
            return '0'

    get_count.short_description = 'Product count'

class GalleryAdmin(admin.TabularInline):
    model = Gallery
    fk_name = 'product'
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'price', 'quantity', 'color', 'get_photo', 'category']
    list_editable = ['price','quantity','color']
    list_display_links = ['id','title']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [GalleryAdmin]

    def get_photo(self,obj):
        if obj.photos:
            try:
                return mark_safe(f'<img src="{obj.photos.first().image.url}" alt="product" width="45px" height= "50px" >')
            except:
                '-'

        else:
            return '-'


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Like)
admin.site.register(Order)
admin.site.register(OrderProduct)