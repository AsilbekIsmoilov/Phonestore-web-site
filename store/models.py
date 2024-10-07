from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Category Name")
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Product Name")
    description = models.TextField(default="No description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Product Price")
    quantity = models.IntegerField(default=0, verbose_name="Product Quantity")
    color = models.CharField(max_length=40, verbose_name="Product Color")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Product Date")
    brand_info = models.TextField(default="No info")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Product Category",
                                 related_name='products')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={"slug": self.slug})

    def get_first_photo(self):
        if self.photos:
            try:
                return self.photos.first().image.url
            except:
                return "https://img.freepik.com/premium-vector/no-photo-available-vector-icon-default-image-symbol-picture-coming-soon-web-site-mobile-app_87543-18055.jpg"
        else:
            return "https://img.freepik.com/premium-vector/no-photo-available-vector-icon-default-image-symbol-picture-coming-soon-web-site-mobile-app_87543-18055.jpg"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to='products/', verbose_name="Photo")

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="User")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="Product")

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"



    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL,blank=True,null=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True,null=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    @property
    def get_cart_total_price(self):
        order_products = self.orderproduct_set.all()
        total_price = sum([product.get_total_price for product in order_products])
        return total_price

    @property
    def get_cart_total_quantity(self):
        order_products = self.orderproduct_set.all()
        total_quantity = sum([product.quantity for product in order_products])
        return total_quantity


    def __str__(self):
        return self.customer.name


    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_total_price(self):
        total_price = self.product.price * self.quantity
        return total_price



    def __str__(self):
        return self.product.title


    class Meta:
        verbose_name = "Order Product"
        verbose_name_plural = "Order Products"


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.address


    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = "Shipping Address"

