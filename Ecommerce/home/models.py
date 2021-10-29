from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
# Create your models here.
CATEGORY=(
    ('NOne','None'),
    ('Mobile','Mobile'),
    ('Electronics','Electronics'),
    ('Laptop','Laptop')
)
class Product(models.Model):
    Name=models.CharField(max_length=60)
    Price=models.IntegerField(default=1000)
    Category=models.CharField(choices=CATEGORY,max_length=40)
    Image=models.ImageField(upload_to='pics')
    Detail=models.TextField()

    def __str__(self):
        return self.Name

class OrderItem(models.Model):
    userid=models.ForeignKey(User,on_delete=SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    dateoforder = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        t=self.userid.username +" "+ str(self.product.id)
        return t


