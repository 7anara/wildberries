from .models import UserProfile, Category, SubCategory, Product, ProductImage, Review, Cart, CartItem
from rest_framework import serializers


from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'phone_number', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

# 1.
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


# 2.
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_image']


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'subCategory_name']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product_image']


class ProductListSerializer(serializers.ModelSerializer):
    product_photo = ProductImageSerializer(many=True, read_only=True)
    subCategory = SubCategoryListSerializer()
    get_average_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField
    class Meta:
        model = Product
        fields = ['id', 'product_photo', 'product_name', 'price', 'subCategory', 'get_average_rating', 'get_count_people']

    def  get_average_rating(self,obj):
        return obj. get_average_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()

# 3.
class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m')
    user = UserProfileSimpleSerializer()
    class Meta:
        model = Review
        fields = ['user', 'rating', 'reviewText', 'created_date']


class SubCategoryDetailSerializer(serializers.ModelSerializer):
    product_sub = ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = SubCategory
        fields = ['subCategory_name', 'product_sub']

class ProductDetailSerializer(serializers.ModelSerializer):
    product_photo = ProductImageSerializer(many=True, read_only=True)
    subCategory = SubCategoryListSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S')
    product_review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'product_photo', 'product_name', 'price', 'article', 'description',
                  'subCategory', 'product_video', 'created_date', 'product_review']



class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_categories = SubCategoryListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name', 'sub_categories']

# 4.





class CartItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, source='product')

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity']



class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']