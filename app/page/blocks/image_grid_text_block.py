from django import forms
from wagtail.core.blocks import CharBlock, StructBlock, StreamBlock, RichTextBlock
from wagtail.images.blocks import ImageChooserBlock

from .base_block import BaseBlock
from .custom_choice_block import CustomChoiceBlock
from .text_column_block import TextColumnBlock

IMAGE_ORDER_CHOICES = (
    ('left', 'Images First'),
    ('right', 'Text First'),
)


class ImageBlockStream(StreamBlock):
    image = ImageChooserBlock()

    class Meta:
        min_num = 1


class ImageGridTextBlock(BaseBlock):
    image_order = CustomChoiceBlock(label='Column Order', choices=IMAGE_ORDER_CHOICES,
                                    default=IMAGE_ORDER_CHOICES[0][0],
                                    required=False, widget=forms.RadioSelect)
    images = ImageBlockStream()
    text_column = TextColumnBlock()

    class Meta:
        template = 'blocks/image_grid_text_block.html'
        label = 'Image Grid Text Block'
        icon = 'square'
