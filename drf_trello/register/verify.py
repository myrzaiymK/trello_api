from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import CustomUser
from drf_trello import serializers
from rest_framework import status
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from .utils import Util
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError


class VerifyEmail(APIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = CustomUser.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)

#
class ResetPasswordView(APIView):
    @swagger_auto_schema(request_body=serializers.ResetPasswordSerializer)
    def post(self, request):
        serializer = serializers.ResetPasswordSerializer(data=request.data)

        if serializer.is_valid():
            # serializer.save()
            user_data = serializer.data
            email = request.data['email']
            # email = serializer.data['email']
            if CustomUser.objects.filter(email=email).exists():
                user = CustomUser.objects.get(email=email)
                uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
                token = PasswordResetTokenGenerator().make_token(user)
                current_site = get_current_site(request=request).domain
                relative_link = reverse('reset_password')
                absurl = 'http://' + current_site + relative_link + "?token=" + str(token)
                email_body = 'HI \n Use link below to reset your password \n' + absurl
                data = {'email_body': email_body, 'to_email': user.email,
                        'email_subject': 'Reset your password '}
                Util.send_email(data)
            return Response({'success': 'We sent you a link to reset password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(APIView):
    pass