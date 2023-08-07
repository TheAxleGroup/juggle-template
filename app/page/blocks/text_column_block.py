from django import forms
from wagtail.core.blocks import CharBlock, RichTextBlock, StructBlock

from .custom_choice_block import CustomChoiceBlock
from .link_block import LinkBlock, StyleLinkBlock
from ..choices import COLUMN_WIDTH_CHOICES

CHECK_CHOICES = (
    ('', 'Dashed list'),
    ('book-style', 'Book Style list'),
)


class TextColumnBlock(StructBlock):
    list_style = CustomChoiceBlock(label='List Style', choices=CHECK_CHOICES,
                                   default=CHECK_CHOICES[0][0],
                                   required=False, widget=forms.Select)
    text_header = CharBlock(required=False)
    text_content = RichTextBlock()
    button_link = LinkBlock()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.column_width = 'col-span-6'

    class Meta:
        template = 'blocks/partials/text_column_block_partial.html'
        label = 'Text Column Block'
        icon = 'font'

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context['self']['column_width'] = 'col-span-6'

        return context


class TextColumnCustomWidthBlock(StructBlock):
    column_width = CustomChoiceBlock(label='Column Width', choices=COLUMN_WIDTH_CHOICES,
                                     default=COLUMN_WIDTH_CHOICES[2][0],
                                     required=False, widget=forms.Select)
    list_style = CustomChoiceBlock(label='List Style', choices=CHECK_CHOICES,
                                   default=CHECK_CHOICES[0][0],
                                   required=False, widget=forms.Select)
    text_header = CharBlock(required=False)
    text_subheader = CharBlock(label='Text sub header', required=False)
    text_content = RichTextBlock()
    button_link = StyleLinkBlock()

    class Meta:
        template = 'blocks/partials/text_column_block_partial.html'
        label = 'Text Column Block'
        icon = 'font'


class TextColumnCustomWidthNoButtonBlock(StructBlock):
    column_width = CustomChoiceBlock(label='Column Width', choices=COLUMN_WIDTH_CHOICES,
                                     default=COLUMN_WIDTH_CHOICES[2][0],
                                     required=False, widget=forms.Select)
    list_style = CustomChoiceBlock(label='List Style', choices=CHECK_CHOICES,
                                   default=CHECK_CHOICES[0][0],
                                   required=False, widget=forms.Select)
    text_header = CharBlock(required=False)
    text_content = RichTextBlock()

    class Meta:
        template = 'blocks/partials/text_column_block_partial.html'
        label = 'Text Column Block'
        icon = 'font'
