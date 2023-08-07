from wagtail.core.blocks import CharBlock, StructBlock, RichTextBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock

from ..blocks.link_block import LinkBlock


class PatternHeroBlock(StructBlock):
    image = ImageChooserBlock()
    header = CharBlock(required=False)
    subheader = CharBlock(label='Sub Header', required=False)

    class Meta:
        template = 'blocks/pattern_hero_block.html'
        label = 'Pattern Hero Block'
        icon = 'image'
