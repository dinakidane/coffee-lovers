from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coffee_experience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def disapprove(self):
        self.approved = False
        self.save()

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'      




