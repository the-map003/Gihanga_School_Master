
from django.db import models
from accounts.models import Users

# Create your models here.
class Supplier(models.Model):
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    contact1=models.CharField(max_length=255)
<<<<<<< HEAD
    contact2=models.CharField(max_length=255)
    created=models.DateTimeField(auto_now_add=True)
    email=models.EmailField(null=True)
    status=models.BooleanField(default=True)
    class Meta:
        ordering=['-created']
=======
    created=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
    class Meta:
        ordering=['created']
>>>>>>> 1c2a8bbe117ff3e572cf253c0116ad0035440f79

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=250)
    class Meta:
        ordering=('-name',)
        verbose_name_plural='Categories'
    def __str__(self):
        return self.name
    
class Item(models.Model):
    category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='item_images', blank=True,null=True)
<<<<<<< HEAD
  
=======
>>>>>>> 1c2a8bbe117ff3e572cf253c0116ad0035440f79
    created_by=models.ForeignKey(Users,related_name='items',on_delete=models.CASCADE)

    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created_at']
    def __str__(self):
        return self.name
    
class PurchaseOrder(models.Model):
    suppliyer=models.ForeignKey(Supplier,related_name='purchase',on_delete=models.CASCADE)
    item=models.ForeignKey(Item,related_name='purchase',on_delete=models.CASCADE)
    quantity=models.IntegerField()
    unit=models.FloatField()
    creator=models.ForeignKey(Users,related_name='purchase',on_delete=models.CASCADE)
    ordered_at=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-ordered_at']
    def __str__(self) :
        return self.item.name

class Stock(models.Model):
    suppliyer=models.ForeignKey(Supplier,related_name='stock',on_delete=models.CASCADE)
    item=models.ForeignKey(Item,related_name='stock',on_delete=models.CASCADE)
    quantity=models.IntegerField()
    unit=models.FloatField()
    creator=models.ForeignKey(Users,related_name='stock',on_delete=models.CASCADE)
    stocked_at=models.DateTimeField(auto_now_add=True)
    status=models.TextField(max_length=255)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-stocked_at']
    def __str__(self) :
        
        return self.item.name   
     
class Stock_Out(models.Model):
        suppliyer=models.ForeignKey(Supplier,related_name='stockout',on_delete=models.CASCADE)
        item=models.ForeignKey(Item,related_name='stockout',on_delete=models.CASCADE)
        quantity=models.IntegerField()
        unit=models.FloatField()
        creator=models.ForeignKey(Users,related_name='stockout',on_delete=models.CASCADE)
        stocked_at=models.DateTimeField(auto_now_add=True)
        status=models.TextField(max_length=255)
        updated_at=models.DateTimeField(auto_now=True)
        class Meta:
            ordering=['-stocked_at']
        def __str__(self) :
            
            return self.item.name   
 
    


        
    