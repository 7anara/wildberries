from django.contrib import admin
from.models import UserProfile, Category, SubCategory, Product,ProductImage,Review,Cart,CartItem
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin

class SubCategoryInline(admin.TabularInline, TranslationInlineModelAdmin):
    model =SubCategory
    extra = 1

@admin.register( Category)
class CategoryAdmin(TranslationAdmin):
    inlines = [SubCategoryInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register( Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductImageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile),
admin.site.register(Review),
admin.site.register(Cart),
admin.site.register(CartItem),
