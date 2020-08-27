from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    # query=request.GET.get('q')
    queryset=TblCommonmaster.objects.all()
    serializer_class=CategorySerializer
    # def get_queryset(self):
  
    #    request=self.request
    #    query=request.GET.get('title')
    #    return TblCommonmaster.objects.filter(title=query)