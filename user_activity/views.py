from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer


class UserActivityView(APIView):
    def get(self, request):
        """
        GET API for users and user activities
        :param request: request object
        :return: json in the specied format
        """

        result = {
            "ok": False,
            "members": []
        }
        qs = CustomUser.objects.all()
        user_data = UserSerializer(qs, many=True).data
        result["members"].extend(user_data)
        return Response(result, status=200)