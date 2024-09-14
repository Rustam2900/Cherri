from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import *
from .serializers import *
from company.models import Banner
is_home = openapi.Parameter('is_home', openapi.IN_QUERY,
                             description="field you want to order by to",
                             type=openapi.TYPE_BOOLEAN)
class BannerListView(APIView):

    def get(self, request, *args, **kwargs):
        banners = Banner.objects.all()
        if not banners.exists():
            return Response({'error': 'No banners found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BannerListSerializer(banners, many=True, context={'request': request})
        return Response(data=serializer.data)


class AboutUsHomeView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsHomeSerializer

    @swagger_auto_schema(manual_parameters=[is_home])
    def get(self, request, *args, **kwargs):
        about_us = AboutUs.objects.last()
        query = self.request.GET.get('is_home', None)
        if query:
            serializer = AboutUsHomeSerializer(about_us, context={'request': request})
        else:
            serializer = AboutUsSerializer(about_us, context={'request': request})
        return Response(data=serializer.data)


class ContactWithUsView(CreateAPIView):
    serializer_class = ContactWithUsSerializer
    queryset = ContactWithUs.objects.all()
    throttle_classes = [UserRateThrottle, ]


class SocialMediaView(ListAPIView):
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()
