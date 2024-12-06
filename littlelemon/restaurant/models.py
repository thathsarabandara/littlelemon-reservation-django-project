from django.db import models

class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guest = models.IntegerField()
    BookingDate = models.DateTimeField()

    def __str__(self):
        return f"Booking Name: {self.Name}, No_of_guest: {self.No_of_guest}"

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()

    def __str__(self):
        return f"Menu Title: {self.Title}, Price: {self.Price}"
