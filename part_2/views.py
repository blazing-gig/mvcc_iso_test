from django.shortcuts import render
from django.db import transaction
from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

from .models import Book

class BookView(APIView):
    def put(self, request):
        with transaction.atomic():
            author_1 = request.data["author_1"]
            Book.objects.filter(author = author_1).update(count = F('count') + 1)

            author_2 = request.data["author_2"]
            Book.objects.filter(author = author_2).update(count = F('count') + 1)

        return Response({})

    def post(self, request):
        with transaction.atomic():
            author = request.data["author_1"]
            count = 16

            Book.objects.filter(
                author = author, count = count
            ).update(count = F('count') - 1)

        return Response({})
