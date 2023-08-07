from django import forms
from django.utils import timezone
from wagtail.core.blocks import CharBlock, StructBlock, RichTextBlock, StreamBlock, BooleanBlock, DateBlock, \
    PageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtailmodelchooser.blocks import ModelChooserBlock

from .base_block import BaseBlock
from .custom_choice_block import CustomChoiceBlock
from .text_column_block import TextColumnCustomWidthBlock
from ..blocks.link_block import LinkBlock
from ..choices import COLUMN_WIDTH_CHOICES


class BaseColumn(StructBlock):
    force_column_to_new_row = BooleanBlock(required=False)
    column_width = CustomChoiceBlock(label='Column Width', choices=COLUMN_WIDTH_CHOICES,
                                     default=COLUMN_WIDTH_CHOICES[2][0],
                                     required=False, widget=forms.Select)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        size = int(context['self']['column_width'][9:])

        context['self']['column_width_int'] = size

        return context


# class HeaderColumn(BaseColumn):
#     column_header = CharBlock()
#
#     class Meta:
#         template = 'blocks/partials/header_column_partial.html'
#         label = 'Icon Content Column'
#         icon = 'fa-circle'


ICON_POSITION_CHOICES = (
    ('top', 'Top Icon'),
    ('side', 'Side Icon'),
)

ICON_SIZE_CHOICES = (
    (' h-9 w-9 ', 'Regular'),
    (' h-20 w-20 ', 'Large'),
)


class IconContent(StructBlock):
    icon = ImageChooserBlock()
    icon_position = CustomChoiceBlock(label='Icon Position', choices=ICON_POSITION_CHOICES,
                                     default=ICON_POSITION_CHOICES[1][0],
                                     required=True, widget=forms.Select)
    icon_size = CustomChoiceBlock(label='Icon Size', choices=ICON_SIZE_CHOICES,
                                     default=ICON_SIZE_CHOICES[0][0],
                                     required=True, widget=forms.Select)
    header = CharBlock(required=False)
    content = RichTextBlock(required=False)


class IconContentStreamBlock(StreamBlock):
    icon_content = IconContent()


class IconContentColumn(BaseColumn):
    icons = IconContentStreamBlock()

    class Meta:
        template = 'blocks/partials/icon_content_column_partial.html'
        label = 'Icon Content Column'
        icon = 'circle'


class ImageColumn(BaseColumn):
    image = ImageChooserBlock()
    circle_image = BooleanBlock(required=False)
    crop_image_to_match_height = BooleanBlock(required=False,
                                              help_text='Crops the image so that it is equal height with the text column.')

    class Meta:
        template = 'blocks/partials/image_column_partial.html'
        label = 'Image Column'
        icon = 'image'


class IconCardColumn(BaseColumn):
    icon = ImageChooserBlock(required=False)
    card_header = CharBlock()
    card_content = RichTextBlock()
    button_link = LinkBlock()

    class Meta:
        template = 'blocks/partials/icon_card_column_partial.html'
        label = 'Icon Card Column'
        icon = 'window-maximize'


class TextColumnBlock(StructBlock):
    force_column_to_new_row = BooleanBlock(required=False)
    text_column = TextColumnCustomWidthBlock()

    class Meta:
        template = 'blocks/partials/multi_block_text_column_partial.html'
        label = 'Text Column'
        icon = 'font'


ASPECT_RATIO_CHOICES = (
    ('56.25%', '16:9'),
    ('75%', '4:3'),
    ('66.66%', '3:2'),
)


class EmbedColumn(BaseColumn):
    embed_link = EmbedBlock()
    embed_aspect_ratio = CustomChoiceBlock(label='Embed Aspect Ratio', choices=ASPECT_RATIO_CHOICES,
                                           default=ASPECT_RATIO_CHOICES[2][0],
                                           required=False, widget=forms.Select)

    class Meta:
        template = 'blocks/partials/embed_column_partial.html'
        label = 'Embed Column'
        icon = 'video'


class FormColumn(BaseColumn):
    form = PageChooserBlock('page.FormPage')

    class Meta:
        template = 'blocks/partials/form_column_partial.html'
        label = 'Form Column'
        icon = 'border-all'


class ColumnStreamBlock(StreamBlock):
    image_column = ImageColumn()
    text_column = TextColumnBlock()
    icon_content_column = IconContentColumn()
    embed_column = EmbedColumn()
    icon_card_column = IconCardColumn()
    form_column = FormColumn()

    class Meta:
        min_num = 1


COLUMN_GAP_CHOICES = (
    ('gap-x-2', 'Small'),
    ('gap-x-4', 'Medium'),
    ('gap-x-8', 'Large'),
    ('gap-x-12', 'Extra Large'),
)


BACKGROUND_CHOICES = (
    ('', 'Off White Background'),
    (' bg-body ', 'Light Gray Background'),
)


class MultiColumnBlock(BaseBlock):
    column_gap = CustomChoiceBlock(label='Column Gap', choices=COLUMN_GAP_CHOICES,
                                   default=COLUMN_GAP_CHOICES[2][0],
                                   required=False, widget=forms.Select)
    bg_color = CustomChoiceBlock(label='Background Color', choices=BACKGROUND_CHOICES,
                                   default=BACKGROUND_CHOICES[0][0],
                                   required=False, widget=forms.Select)
    block_link = LinkBlock()
    block_header = CharBlock(required=False)
    columns = ColumnStreamBlock()

    class Meta:
        template = 'blocks/multi_column_block.html'
        label = 'Multi Column Block'
        icon = 'columns'
