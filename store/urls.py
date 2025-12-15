from django.urls import path, include
from .views import (UserProfileView, CategoryListAPIView, CategoryDetailAPIView,
                    SubCategoryListAPIView, SubCategoryDetailAPIView,
                    ProductListAPIView, ProductDetailAPIView, ProductImageView, ReviewView,
                    CartView, CartItemView, RegisterView, LoginView, LogoutView)
from rest_framework import routers


router = routers.SimpleRouter()
router.register(f'user', UserProfileView, basename='user')
router.register(f'productImage', ProductImageView, basename='productImage')
router.register(f'reviewText', ReviewView, basename='reviewText')



urlpatterns = [
    path('', include(router.urls)),

    path('register', RegisterView.as_view(), name='registrations'),
    path('login', LoginView.as_view(), name = 'login'),
    path('logout', LogoutView.as_view(), name = 'logout'),



    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name = 'category_detail'),
    path('sub_category/', SubCategoryListAPIView.as_view(), name='sub_category_list'),
    path('sub_category/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='sub_category_detail'),
    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart_detail'),
    path('cart_item/', CartItemView.as_view({'get':'list', 'post':'create'})),
    path('cart_item/<int:pk>/', CartItemView.as_view({'put':'update', 'delete':'destroy'}))

]

