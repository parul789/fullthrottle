from django.urls import path
from .views import UserActivityView

urlpatterns = [
    path('users-activity', UserActivityView.as_view())
]