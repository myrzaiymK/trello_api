from rest_framework import generics, response
from drf_trello import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from trello_app.models import *
from users.models import CustomUser
from rest_framework import status
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.http import Http404



class UserList(APIView):
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = ['username', 'email']

    def get(self, request):
        snippets = CustomUser.objects.all()
        filtered_qs = self.filter_queryset(snippets)
        serializer = serializers.UserSerializer(filtered_qs, many=True)
        return Response(serializer.data)

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    @swagger_auto_schema(request_body=serializers.UserSerializer)
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data
            user = CustomUser.objects.get(email=user_data['email'])

            token = RefreshToken.for_user(user).access_token
            relativeLink = reverse('email-verify')

            current_site = get_current_site(request).domain
            absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
            email_body = 'HI ' + user.username + ' Use link below to activate your account \n' + absurl
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Verify your email '}
            Util.send_email(data)
            return Response(user_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = serializers.UserSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = serializers.UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

