from django.db import models

# make migrations  - create changes and store in files
# migrate - apply the pending changes created by makemigrations 

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122,null=True, blank=True)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=99.99)
    image = models.ImageField(upload_to='product_images/', default='default.jpg')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class FeedbackForm(models.Model):
    User_name = models.CharField(max_length=25)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField()
    Image = models.ImageField(upload_to='media/', blank=True)
    

    def __str__(self):
        return self.User_name

class Payment(models.Model):
    method = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')
    timestamp = models.DateTimeField(auto_now_add=True)

class Flavor(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/')

class LoginRecord(models.Model):
    Username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.Username

class SignupRecord(models.Model):
    Username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.Username

class IceCream(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='static/', blank=True, null=True)

    @property
    def discounted_price(self):
        return self.price * (100 - self.discount_percent) / 100
    
