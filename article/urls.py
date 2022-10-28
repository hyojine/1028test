from django.urls import path
from article.views import ArticleView
# from article import views



urlpatterns = [
    path('', ArticleView.as_view(), name='articleview'),
]
