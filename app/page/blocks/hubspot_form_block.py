from wagtail.core.blocks import CharBlock, StructBlock, StreamBlock, RichTextBlock, BooleanBlock, TextBlock
from wagtail.images.blocks import ImageChooserBlock
from django import forms

from .base_block import BaseBlock
from .custom_choice_block import CustomChoiceBlock
from .link_block import LinkBlock, RequiredLinkBlock
from ..choices import COLUMN_WIDTH_CHOICES


class HubspotFormBlock(BaseBlock):
    block_header = CharBlock(required=False)
    block_content = RichTextBlock(required=False)
    hubspot_code = TextBlock()

    class Meta:
        template = 'blocks/hubspot_form_block.html'
        label = 'Hubspot Form Block'
        icon = 'th'
