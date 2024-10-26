from django.db import models

# Create your models here.
class ItemList(models.Model):
    Catagory_name=models.CharField(max_length=20)
    def __str__(self):
        return self.Catagory_name

class Items(models.Model):
    ItemName=models.CharField(max_length=20)
    Desciption=models.TextField(blank=False)
    price=models.IntegerField()
    Catagory=models.ForeignKey(ItemList, related_name="Name",on_delete=models.CASCADE)
    Image=models.ImageField(upload_to="Items/")
    def __str__(self):
        return self.ItemName


class AboutUs(models.Model):
    Desciption=models.TextField(blank=False)


class Feedback(models.Model):
    User_name=models.CharField(max_length=20)
    Desciption=models.TextField(blank=False)
    Rating=models.IntegerField()

    def __str__(self):
        return self.User_name

class BookTable(models.Model):
    Name=models.CharField(max_length=20)
    Phone_Number=models.IntegerField()
    Email=models.EmailField()
    Total_Person=models.IntegerField()
    Booking_Date=models.DateField()

    def __str__(self):
        return self.Name