from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(validators=[MinValueValidator(15), MaxValueValidator(80)], null=True, blank=True)
    phone_number = PhoneNumberField()
    STATUS_CHOICES = (
           ('gold', 'gold'),
           ('silver', 'silver'),
           ('bronze', 'bronze'),
           ('simple', 'simple'),
    )

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='simple')
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'



class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)
    category_image = models.ImageField(upload_to='category_image/', null=True, blank=True)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    subCategory_name = models.CharField(max_length=54)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')

    def __str__(self):
        return self.subCategory_name


class Product(models.Model):
    product_name = models.CharField(max_length=64)
    price = models.PositiveIntegerField()
    article = models.PositiveIntegerField(unique=True)
    product_video = models.FileField(upload_to='video/', null=True, blank=True)
    description = models.TextField()
    subCategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE, related_name='product_sub')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_name} {self.subCategory}'


    def get_average_rating(self):
        review = self.product_review.all()
        if review.exists():
            return round(sum(i.rating for i in review) / review.count(),2)
        return 0

    def get_count_people(self):
        return self.product_review.count()



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_photo')
    product_image = models.ImageField(upload_to='product_image/', null= True, blank=True)


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_review')
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1,6)], null=True, blank=True)
    reviewText = models. TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.rating}'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f'{self.product}-{self.quantity}'
