from wagtail.core.blocks import CharBlock, StructBlock, RichTextBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock

from ..blocks.link_block import LinkBlock


class ImageBlockStream(StreamBlock):
    image = ImageChooserBlock()

    class Meta:
        min_num = 1
        max_num = 5


class CollageHeroBlock(StructBlock):
    images = ImageBlockStream()
    header = CharBlock(required=False)
    subheader = CharBlock(label='Sub Header')
    button_link = LinkBlock()

    class Meta:
        template = 'blocks/collage_hero_block.html'
        label = 'Collage Hero Block'
        icon = 'images'
