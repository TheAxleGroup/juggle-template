from django import forms
from wagtail.core.blocks import CharBlock, StructBlock, StreamBlock, FieldBlock, PageChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtailgeowidget import geocoders

from .base_block import BaseBlock
from .custom_choice_block import CustomChoiceBlock
from .link_block import LinkBlock, RequiredLinkBlock
from django.db import models
from wagtailgeowidget.blocks import GoogleMapsBlock, GeoZoomBlock, GeoAddressBlock


class AddressMapBlock(StructBlock):
    title = CharBlock()
    phone = CharBlock(required=False)
    fax = CharBlock(required=False)
    address = GeoAddressBlock(geocoder=geocoders.GOOGLE_MAPS)
    zoom = GeoZoomBlock(required=False)
    map = GoogleMapsBlock(address_field='address', zoom_field='zoom')

    class Meta:
        icon = 'map'


class MapBlockStream(StreamBlock):
    map_block = AddressMapBlock()

    class Meta:
        min_num = 1
        icon = 'map'


class FormMapBlock(BaseBlock):
    form_header = CharBlock()
    form_subheader = CharBlock(required=False)
    form = PageChooserBlock('page.FormPage')
    location_header = CharBlock()
    location_subheader = CharBlock(required=False)
    maps = MapBlockStream()

    class Meta:
        template = 'blocks/form_map_block.html'
        label = 'Form Map Block'
        icon = 'border-all'
