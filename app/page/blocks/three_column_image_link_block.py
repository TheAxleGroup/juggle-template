from wagtail.core.blocks import CharBlock, StructBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock

from .base_block import BaseBlock
from .link_block import LinkBlock, RequiredLinkBlock


class ImageLinkBlock(StructBlock):
    image = ImageChooserBlock()
    block_title = CharBlock()
    link = RequiredLinkBlock()

    class Meta:
        label = 'Image Block'
        icon = 'link'


class ImageLinkBlockStream(StreamBlock):
    image_link_block = ImageLinkBlock()

    class Meta:
        min_num = 1


class ThreeColumnIconTextBlock(BaseBlock):
    block_header = CharBlock()
    button_link = LinkBlock()
    image_links = ImageLinkBlockStream()

    class Meta:
        template = 'blocks/three_column_image_link_block.html'
        label = 'Three Image Link Block'
        icon = 'link'
