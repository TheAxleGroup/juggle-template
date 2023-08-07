from django import forms
from wagtail.core.blocks import CharBlock, StructBlock, StreamBlock, RichTextBlock, BooleanBlock
from wagtail.images.blocks import ImageChooserBlock

from .base_block import BaseBlock
from .custom_choice_block import CustomChoiceBlock
from .text_column_block import TextColumnBlock


class IconTextBlock(StructBlock):
    icon = ImageChooserBlock()
    text = CharBlock()

    class Meta:
        label = 'Icon Text Block'
        icon = 'circle'


class IconBlockStream(StreamBlock):
    icon = IconTextBlock()

    class Meta:
        min_num = 1


ITEM_PER_ROW_CHOICES = (
    (' item-2 ', '2 items per row'),
    (' item-3 ', '3 items per row'),
    (' item-4 ', '4 items per row'),
)


class IconTextRowBlock(BaseBlock):
    block_header = CharBlock()
    items_per_row = CustomChoiceBlock(label='Items Per Row', choices=ITEM_PER_ROW_CHOICES,
                                      default=ITEM_PER_ROW_CHOICES[2][0],
                                      required=False, widget=forms.Select)
    center_items = BooleanBlock(required=False)
    icons = IconBlockStream()

    class Meta:
        template = 'blocks/icon_text_row_block.html'
        label = 'Icon Text Row Block'
        icon = 'circle'
