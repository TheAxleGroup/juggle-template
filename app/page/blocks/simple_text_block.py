from wagtail.core.blocks import CharBlock, StructBlock, StreamBlock, RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from django import forms

from .base_block import BaseBlock
from .custom_choice_block import CustomChoiceBlock
from .link_block import LinkBlock, RequiredLinkBlock
from .text_column_block import TextColumnCustomWidthBlock, TextColumnCustomWidthNoButtonBlock
from ..choices import COLUMN_WIDTH_CHOICES


class LinkCard(StructBlock):
    card_content = RichTextBlock()
    link = RequiredLinkBlock()

    class Meta:
        icon = 'link'


class CustomListStreamBlock(StreamBlock):
    card = LinkCard()

    class Meta:
        required = False
        max_num = 2
        icon = 'link'


class SquareImageStreamBlock(StreamBlock):
    image = ImageChooserBlock()

    class Meta:
        required = False
        icon = 'image'


BACKGROUND_CHOICES = (
    ('', 'Off White Background'),
    (' bg-body ', 'Light Gray Background'),
)


class SimpleTextBlock(BaseBlock):
    bg_color = CustomChoiceBlock(label='Background Color', choices=BACKGROUND_CHOICES,
                                   default=BACKGROUND_CHOICES[0][0],
                                   required=False, widget=forms.Select)
    image_background = ImageChooserBlock(required=False)
    text_column = TextColumnCustomWidthNoButtonBlock()
    link_cards = CustomListStreamBlock()
    square_images = SquareImageStreamBlock()
    button_link = LinkBlock()

    class Meta:
        template = 'blocks/simple_text_block.html'
        label = 'Simple Text Block'
        icon = 'font'
