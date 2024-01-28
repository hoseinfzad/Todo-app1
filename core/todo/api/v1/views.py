from ...models import Task

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination
from .serializers import TaskSerializer


class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.filter(complete=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user', 'title', 'complete']
    search_fields = ['title']
    ordering_fields = ['created_date']
    pagination_class = DefaultPagination
