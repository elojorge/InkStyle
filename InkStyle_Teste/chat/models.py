from django.db import models
from users.models import User

# Create your models here.


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.user.username}: {self.content[:20]}...'
