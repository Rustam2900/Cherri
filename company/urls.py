from django.urls import path
from .views import BannerListView, AboutUsHomeView, SocialMediaView, ContactWithUsView

urlpatterns = [
    path("banners/", BannerListView.as_view(), name="banner-list"),
    path('about-us/', AboutUsHomeView.as_view(), name="about-us-home"),
    path('social-media/', SocialMediaView.as_view(), name='social-media'),
    path('contact-us', ContactWithUsView.as_view(), name='contact-us'),
]
