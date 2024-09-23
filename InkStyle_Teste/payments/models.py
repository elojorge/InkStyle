from django.db import models
from users.models import User

# Create your models here.


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])
    transaction_id = models.CharField(max_length=100, unique=True)

    def str(self):
        return f'Payment {self.transaction_id} by {self.user.username} - {self.amount} {self.get_status_display()}'