from django import forms
from wagtail.core.blocks import CharBlock, StructBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock

from .base_block import BaseBlock
from .custom_choice_block import CustomChoiceBlock
from .link_block import LinkBlock, RequiredLinkBlock

COLUMN_WIDTH_CHOICES = (
    ('col-span-3', '3/12 Width'),
    ('col-span-4', '4/12 Width'),
    ('col-span-6', '6/12 Width'),
)


class IconLinkBlock(StructBlock):
    block_width = CustomChoiceBlock(label='Column Width', choices=COLUMN_WIDTH_CHOICES,
                                    default=COLUMN_WIDTH_CHOICES[2][0],
                                    required=False, widget=forms.Select)
    icon = ImageChooserBlock(required=False)
    icon_hover = ImageChooserBlock(required=False)
    icon_title = CharBlock()
    link = RequiredLinkBlock()

    class Meta:
        label = 'Icon Link Block'
        icon = 'link'


class IconLinkBlockStream(StreamBlock):
    icon_link_block = IconLinkBlock()

    class Meta:
        min_num = 1


class IconGridLinkBlock(BaseBlock):
    block_header = CharBlock(required=False)
    icon_links = IconLinkBlockStream()

    class Meta:
        template = 'blocks/icon_grid_link_block.html'
        label = 'Icon Grid Link Block'
        icon = 'th'
