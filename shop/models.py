from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

class checkout(models.Model):
    order_id = models.AutoField
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    amount = models.IntegerField(default=0)
    email = models.EmailField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111)

    def __str__(self):
        return self.name


class Form(models.Model):
    id = models.AutoField
    Email = models.CharField(max_length=5000)
    F_name = models.CharField(max_length=90)
    L_name = models.CharField(max_length=90, default="a")
    SubjectC = models.CharField(max_length=90, default="a")
    Message = models.CharField(max_length=90, default="a")

    def __str__(self):
        return self.Email
    
class Coupon(models.Model):
    id = models.AutoField
    coupon_name = models.CharField(max_length=5000)
    discount_per = models.IntegerField(default=0)

    def __str__(self):
        return self.coupon_name

class Brand(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=5000)
    type = models.CharField(max_length=90)

    def __str__(self):
        return self.name


class Orders(models.Model):
    id = models.AutoField
    itemsjson = models.CharField(max_length=5000)
    product_id = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    address = models.CharField(max_length=90)
    phone = models.CharField(max_length=90)
    state = models.CharField(max_length=90)
    city = models.CharField(max_length=90)
    Zipcode = models.CharField(max_length=90)
    amount = models.FloatField(default=0)
    coupon = models.CharField(max_length=90, default="")


    # def __str__(self):
    #     return self.name
