from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.users.models import User



class Category(models.Model):
    categories_name = models.CharField(db_index=True, max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    category_image = models.ImageField(upload_to='product_banner', blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categories_name



class Sub_Category(models.Model):
    categories = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=300)
    featured_department=models.BooleanField()
    slug = models.SlugField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product_name

class Product(models.Model):
    product_id = models.ForeignKey(Sub_Category, related_name='product_id', on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    title = models.CharField(max_length=100,unique=True)
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])
    discount=models.IntegerField(blank=True,null=True)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='products_image', blank=False)
    additional_description = models.TextField(max_length=5000)
    feature_product=models.BooleanField()
    like = models.ManyToManyField(User, blank=True, related_name='product_like')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    CATEGORIES_CHOICES = (
        ('GN', 'General '),
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
    )
    size = models.CharField(choices=CATEGORIES_CHOICES, null=True, max_length=100)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000)], null=True)

    def __str__(self):
        return self.brand_name

    @property
    def discount_price(self):
        if self.discount:
             sub_total = (self.discount * self.price) / 100
             total_price = self.price - sub_total
             return total_price
        return 0

class Banner(models.Model):
    name = models.CharField(max_length=32, blank=False)
    discount = models.IntegerField(blank=True,null=True)
    valid_from = models.DateTimeField(blank=False)
    valid_to = models.DateTimeField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField()
    image = models.ImageField(upload_to='background_image', blank=False)

    def __str__(self):
        return self.name

class Product_review(models.Model):
    review_object=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    comment = models.CharField(max_length=512)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
    email = models.EmailField()
