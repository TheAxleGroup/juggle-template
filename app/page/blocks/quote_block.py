from wagtail.core.blocks import CharBlock, StructBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock
from django import forms

from .base_block import BaseBlock
from .custom_choice_block import CustomChoiceBlock
from .link_block import LinkBlock, RequiredLinkBlock
from .text_column_block import TextColumnCustomWidthBlock
from ..choices import COLUMN_WIDTH_CHOICES


class QuoteBlock(BaseBlock):
    quote_text = CharBlock()
    quote_author_image = ImageChooserBlock(required=False)
    quote_author_name = CharBlock()
    quote_author_title = CharBlock(required=False)
    quote_author_title_2 = CharBlock(required=False)

    class Meta:
        template = 'blocks/quote_block.html'
        label = 'Quote Block'
        icon = 'quote-left'
