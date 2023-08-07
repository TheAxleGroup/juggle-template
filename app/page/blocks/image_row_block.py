from wagtail.core.blocks import CharBlock, StructBlock, StreamBlock, RichTextBlock
from wagtail.images.blocks import ImageChooserBlock

from .base_block import BaseBlock
from .text_column_block import TextColumnBlock


class ImageBlockStream(StreamBlock):
    image = ImageChooserBlock()

    class Meta:
        min_num = 1
        max_num = 6


class ImageRowBlock(BaseBlock):
    images = ImageBlockStream()

    class Meta:
        template = 'blocks/image_row_block.html'
        label = 'Image Row Block'
        icon = 'arrows-alt-h'
