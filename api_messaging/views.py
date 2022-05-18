from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.utils import timezone

from .models import Message
from .serializers import MessageSerializer, UserRegisterSerializers


class MessageView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):

        if within_message_limit(request.user):
            request.data['created_by'] = request.user.id
            if request.data.get('id', None):
                message = Message.objects.get(id=request.data['id'])
                serializer = MessageSerializer(message, data=request.data)
            else:
                serializer = MessageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": "Message Limit Exceeded"}, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterView(CreateAPIView):

    serializer_class = UserRegisterSerializers
    model = User


def within_message_limit(user):
    limit = timezone.now() - timezone.timedelta(hours=1)
    messages = Message.objects.filter(created_by=user, created_at__gte=limit)
    return messages.count() < 10
