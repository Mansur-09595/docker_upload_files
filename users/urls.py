from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import BookList, BookDetail
from . import views

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('api/', BookList.as_view(), name='api'),
    path('api/<int:pk>/', BookDetail.as_view()),
    path('upload/', views.upload, name='upload'),
    path('', views.book_list, name='book_list'),
    path('books/upload', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

