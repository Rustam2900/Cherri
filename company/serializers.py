from rest_framework import serializers

from company.models import Banner, AboutUs, AboutUsGallery, SocialMedia, ContactWithUs
from common.serializers import MediaURLSerializer
from product.models import Product


class BannerListSerializer(serializers.ModelSerializer):
    bg_image = MediaURLSerializer()
    class Meta:
        model = Banner
        exclude = ('id', )
        read_only_fields = ('title', 'subtitle', 'bg_image')


class AboutUsGallerySerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()
    class Meta:
        model = AboutUsGallery
        fields = ('image', )

class AboutUsHomeSerializer(serializers.ModelSerializer):
    galleries = serializers.SerializerMethodField()
    class Meta:
        model = AboutUs
        fields = ('desc', 'galleries')

    def get_galleries(self, obj):
        return AboutUsGallerySerializer(obj.galleries.all().order_by('?')[:6], many=True, context=self.context).data


class AboutUsSerializer(serializers.ModelSerializer):
    galleries = serializers.SerializerMethodField()

    class Meta:
        model = AboutUs
        fields = ("desc", "video", "galleries")


    def get_galleries(self, obj):
        return AboutUsGallerySerializer(obj.galleries.all(), many=True, context=self.context).data


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ("link", "icon")


class ContactWithUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactWithUs
        fields = ("full_name", "phone_number", "subject", "message")