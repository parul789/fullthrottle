from rest_framework import serializers
from datetime import datetime
from .models import CustomUser, UserActivity


class UserActivitySerializer(serializers.Serializer):
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    class Meta:
        model = UserActivity
        fields = ["start_time", "end_time"]

    def get_start_time(self, instance):
        return instance.start_datetime

    def get_end_time(self, instance):
        return instance.end_datetime


class UserSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    real_name = serializers.SerializerMethodField()
    tz = serializers.SerializerMethodField()
    activity_periods = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ["id", "real_name", "tz", "activity_periods"]

    def get_id(self, instance):
        return instance.user_id

    def get_real_name(self, instance):
        return f"{instance.first_name} {instance.last_name}"

    def get_tz(self, instance):
        return instance.time_zone

    def get_activity_periods(self, instance):
        convert = lambda x: datetime.strftime(x, "%b %w %Y %I:%M%p")
        user_activities = instance.user_activities.all().values("start_datetime", "end_datetime")
        for acts in user_activities:
            if acts.get("start_datetime") and acts.get("end_datetime"):
                acts["start_datetime"] = convert(acts["start_datetime"])
                acts["end_datetime"] = convert(acts["end_datetime"])
        return user_activities