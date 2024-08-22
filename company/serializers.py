from rest_framework import serializers

from company.models import Banner, AboutUs, AboutUsGallery
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


