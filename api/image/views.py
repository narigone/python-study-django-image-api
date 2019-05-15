from image.models import Image
from image.serializers import ImageSerializer

from django.shortcuts import render

import json

from rest_framework import viewsets, views
from rest_framework.parsers import MultiPartParser, FormParser
 
class ImageViewSet(viewsets.ModelViewSet): 
    queryset = Image.objects.all().order_by('-created_at')
    serializer_class = ImageSerializer