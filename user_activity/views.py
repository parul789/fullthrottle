from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer


class UserActivityView(APIView):
    def get(self, request):
        members = []
        qs = CustomUser.objects.all()
        user_activity_qs = UserSerializer(qs, many=True).data
        members.extend(user_activity_qs)
        return Response(members, status=200)