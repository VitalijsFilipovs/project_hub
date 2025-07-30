# tasks/pagination.py
from rest_framework.pagination import CursorPagination

class CategoryCursorPagination(CursorPagination):
    page_size = 6
    ordering = '-created_at'
