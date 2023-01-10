from datetime import timezone, timedelta
from django.db.models import Count
from drf_trello.card import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from trello_app.models import *
from users.models import CustomUser
from rest_framework import status, filters
from rest_framework.settings import api_settings
from django.contrib.auth.decorators import login_required



class CardList(APIView):
    def get(self, request):
        snippets = Card.objects.all()
        serializer = serializers.CardSerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=serializers.CardSerializer)
    def post(self, request):
        serializer = serializers.CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LabelList(APIView):
    def get(self, request):
        snippets = Label.objects.all()
        serializer = serializers.LabelSerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=serializers.LabelSerializer)
    def post(self, request):
        serializer = serializers.LabelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LabelCardList(APIView):
    def get(self, request):
        snippets = LabelCard.objects.all()
        serializer = serializers.LabelCardSerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=serializers.LabelCardSerializer)
    def post(self, request):
        serializer = serializers.LabelCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CheckListView(APIView):
    def get(self, request):
        snippets = CheckList.objects.all()
        serializer = serializers.CheckListSerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=serializers.CheckListSerializer)
    def post(self, request):
        serializer = serializers.CheckListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LabelColorList(APIView):
    def get(self, request):
        snippets = LabelColor.objects.all()
        serializer = serializers.LabelColorSerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=serializers.LabelColorSerializer)
    def post(self, request):
        serializer = serializers.LabelColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CheckListCardView(APIView):
    def get(self, request):
        snippets = CheckListCard.objects.all()
        serializer = serializers.CheckListCardSerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=serializers.CheckListCardSerializer)
    def post(self, request):
        serializer = serializers.CheckListCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttachmentList(APIView):
    def get(self, request):
        snippets = Attachment.objects.all()
        serializer = serializers.AttachmentSerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=serializers.AttachmentSerializer)
    def post(self, request):
        serializer = serializers.AttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttchmentCardList(APIView):
    def get(self, request):
        snippets = AttachmentCard.objects.all()
        serializer = serializers.AttachCardSerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=serializers.AttachCardSerializer)
    def post(self, request):
        serializer = serializers.AttachCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
