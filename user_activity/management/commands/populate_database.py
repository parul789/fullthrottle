import os
import json

from django.core.management.base import BaseCommand

from datetime import datetime
from user_activity.models import UserActivity, CustomUser

CURRENT_DIRECTORY = os.getcwd()


class Command(BaseCommand):
    help = 'Populate database with dummy data.'

    def handle(self, *args, **kwargs):
        """
        Flushes out data from UserActivity and CustomUser table and
        re-populates these tables with fresh data
        """
        CustomUser.objects.all().delete()
        UserActivity.objects.all().delete()

        users = json.loads(open(f"{CURRENT_DIRECTORY}/fullthrottle/dummy_data/user.json", "r").read())
        activities = json.loads(open(f"{CURRENT_DIRECTORY}/fullthrottle/dummy_data/activity.json", "r").read())
        convert_to_datetime = lambda datetime_str: datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

        for user in users:
            user_instance = CustomUser.objects.create(**user)
            for acts in activities:
                UserActivity.objects.create(
                    start_datetime=convert_to_datetime(acts["start_datetime"]),
                    end_datetime=convert_to_datetime(acts["end_datetime"]),
                    user=user_instance
                )