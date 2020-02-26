from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MessageDetail, MessageList, api_root

urlpatterns = [
    path('messages/', MessageList.as_view()),
    path('messages/single/<int:pk>/', MessageDetail.as_view()),
    path('', api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
