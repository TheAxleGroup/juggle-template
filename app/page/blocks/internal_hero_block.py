from django import forms
from wagtail.core.blocks import CharBlock, StructBlock, RichTextBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock

from .custom_choice_block import CustomChoiceBlock
from ..blocks.link_block import LinkBlock


INTERNAL_HERO_CHOICES = (
    ('left-hero', 'Left Style Hero'),
    ('center-hero', 'Center Style Hero'),
)


class InternalHeroBlock(StructBlock):
    header = CharBlock(required=False)
    subheader = RichTextBlock()
    desktop_image = ImageChooserBlock()
    mobile_image = ImageChooserBlock(required=False)
    internal_hero_style = CustomChoiceBlock(label='Internal Hero Style', choices=INTERNAL_HERO_CHOICES,
                                           default=INTERNAL_HERO_CHOICES[0][0],
                                           required=False, widget=forms.Select)

    class Meta:
        template = 'blocks/internal_hero_block.html'
        label = 'Internal Hero Block'
        icon = 'square'
