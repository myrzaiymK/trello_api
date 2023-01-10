from drf_trello import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from trello_app.models import *
from rest_framework import status, filters
from rest_framework.settings import api_settings



class RecentViewsView(APIView):
    def get(self, request):
        snippets = RecentViews.objects.all().order_by('-views_time')[:6]
        serializer = serializers.RecentViewsSerializer(snippets, many=True)
        return Response(serializer.data)


class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('title_only'):
            return ['title']
        return super().get_search_fields(view, request)


class BoardList(APIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        # snippets = Board.objects.all()
        snippets = Board.objects.filter()
        serializer = serializers.BoardSerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=serializers.BoardSerializer)
    def post(self, request):
        serializer = serializers.BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ColumnList(APIView):
    def get(self, request):
        snippets = Column.objects.all()
        serializer = serializers.ColumnSerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=serializers.ColumnSerializer)
    def post(self, request):
        serializer = serializers.ColumnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CommentList(APIView):
    def get(self, request):
        snippets = Comment.objects.all()
        serializer = serializers.CommentSerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=serializers.BoardSerializer)
    def post(self, request):
        serializer = serializers.CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class MemberList(APIView):
    def get(self, request):
        snippets = Member.objects.all()
        serializer = serializers.MemberSerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=serializers.MemberSerializer)
    def post(self, request):
        serializer = serializers.MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArchiveList(APIView):
    def get(self, request):
        snippets = Board.objects.all()
        archive_boards = []
        for i in snippets:
            if i.archive is True:
                archive_boards.append(i)
        serializer = serializers.BoardSerializer(archive_boards, many=True)
        return Response(serializer.data)


class FavoriteList(APIView):
    def get(self, request):
        snippets = Favourites.objects.all()
        serializer = serializers.FavouriteSerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=serializers.FavouriteSerializer)
    def post(self, request):
        serializer = serializers.FavouriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

