from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    user_id = models.CharField(max_length=7)
    time_zone = models.CharField( max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id


class UserActivity(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="user_activities"
    )
    start_datetime = models.DateTimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"
