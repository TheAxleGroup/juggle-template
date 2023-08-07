from wagtail.core.blocks import CharBlock, StructBlock, RichTextBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock

from ..blocks.link_block import LinkBlock


class SimpleHeroBlock(StructBlock):
    desktop_image = ImageChooserBlock()
    mobile_image = ImageChooserBlock(required=False)
    header = CharBlock(required=False)
    subheader = CharBlock(label='Sub Header', required=False)

    class Meta:
        template = 'blocks/simple_hero_block.html'
        label = 'Simple Hero Block'
        icon = 'image'
