from django.db import models
from users.models import User

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tattoo_artist = models.CharField(max_length=100)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed')])

    def str(self):
        return f'Booking by {self.user.username} with {self.tattoo_artist} on {self.date}'