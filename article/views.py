# from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from article.serializers import ArticleSerializer
from rest_framework.views import APIView
from .models import Article
# Create your views here.


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
