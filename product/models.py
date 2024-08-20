from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import Media
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Product(models.Model):
    title = models.CharField(_('title'), max_length=255)
    desc = models.TextField(_('description'), max_length=255)
    size = models.CharField(_('size'), max_length=255)
    image = models.OneToOneField(Media, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Product')


class ProductAttribute(models.Model):
    title = models.CharField(_('title'), max_length=255)
    value = models.CharField(_('value'), max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product Attribute')
        verbose_name_plural = _('Product Attribute')


class WebOrder(models.Model):
    full_name = models.CharField(_('full_name'), max_length=255)
    phone_number = PhoneNumberField(_('phone_number'), max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Web Order ')
        verbose_name_plural = _('Web Order ')