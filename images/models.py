from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Image(models.Model):
    CATEGORY_CHOICES = (
        ('long', 'Long'),
        ('medium', 'Medium'),
        ('tall', 'Tall'),
    )

    title = models.CharField(max_length=255, name='title', default=None)
    image = models.ImageField(upload_to='my_images/')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image_description = models.TextField(blank=True, max_length=255)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    larger_image = models.ImageField(upload_to='larger-images/', blank=True, null=True)


    def __str__(self):
        return self.category

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    wedding_venue = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    time_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.message}"

# Tracking and Tags
class TrackingScript(models.Model):
    name = models.CharField(max_length=255, help_text="A descriptive name for the script.")
    script = models.TextField(help_text="The HTML/JavaScript code.")
    active = models.BooleanField(default=True, help_text="Indicates if the script should be active.")
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name


# Discounts and Offers
class Discount(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    gif_image = models.ImageField(upload_to='discount_gifs/', blank=True, null=True)
    active = models.BooleanField(default=False)
    author= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def is_active(self):
        # Check if current time is within the discount period
        return self.active and self.start_date <= timezone.now() <= self.end_date

    def __str__(self):
        return self.title