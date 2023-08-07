from wagtail.core.blocks import CharBlock, StructBlock, StreamBlock, BooleanBlock
from wagtail.images.blocks import ImageChooserBlock
from django import forms

from .base_block import BaseBlock
from .custom_choice_block import CustomChoiceBlock
from .link_block import LinkBlock, RequiredLinkBlock
from .text_column_block import TextColumnCustomWidthBlock, TextColumnBlock
from ..choices import COLUMN_WIDTH_CHOICES

IMAGE_ORDER_CHOICES = (
    ('left', 'Desktop Image First'),
    ('right', 'Desktop Text First'),
)


class ListBullet(StructBlock):
    icon = ImageChooserBlock()
    text = CharBlock()


class CustomListStreamBlock(StreamBlock):
    bullet_item = ListBullet()

    class Meta:
        required = False


class ImageTextBlock(BaseBlock):
    image_order = CustomChoiceBlock(label='Desktop Column Order', choices=IMAGE_ORDER_CHOICES,
                                    default=IMAGE_ORDER_CHOICES[0][0],
                                    required=False, widget=forms.RadioSelect)
    image_overflow = BooleanBlock(required=False ,help_text='Allows the image to overflow out of the container, touching the side of the window')
    image = ImageChooserBlock()
    crop_image_to_match_height = BooleanBlock(required=False,
                                              help_text='Crops the image so that it is equal height with the text column.')
    text_column = TextColumnBlock()
    custom_list = CustomListStreamBlock()

    class Meta:
        template = 'blocks/image_text_block.html'
        label = 'Image Text Block'
        icon = 'align-justify'
