from .models import Category, SubCategory, Product
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)



@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('subCategory_name',)



@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description')




