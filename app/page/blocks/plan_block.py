from wagtail.core.blocks import CharBlock, StructBlock, RichTextBlock, StreamBlock, BooleanBlock
from wagtail.images.blocks import ImageChooserBlock
from django import forms

from .base_block import BaseBlock
from .custom_choice_block import CustomChoiceBlock
from ..blocks.link_block import LinkBlock

PLAN_COLOR_CHOICES = (
    ('red', 'Red'),
    ('yellow', 'Yellow'),
    ('green', 'Green'),
    ('azure', 'Blue'),
)


class Plan(StructBlock):
    plan_title = CharBlock()
    plan_subtitle = RichTextBlock()
    price_month = CharBlock()
    price_year = CharBlock()
    plan_desc = RichTextBlock()
    month_url = CharBlock()
    year_url = CharBlock()
    button_text = CharBlock()

    plan_color = CustomChoiceBlock(label='Type', choices=PLAN_COLOR_CHOICES, default=PLAN_COLOR_CHOICES[0][0],
                                   widget=forms.RadioSelect)
    most_popular = BooleanBlock(required=False)

    class Meta:
        label = 'Plan'
        icon = 'image'


class PlanStreamBlock(StreamBlock):
    plan = Plan()

    class Meta:
        max_num = 4


class PlanBlock(StructBlock):
    header = CharBlock(required=False)
    subheader = CharBlock(required=False)
    plans = PlanStreamBlock()

    class Meta:
        template = 'blocks/plan_block.html'
        label = 'Plan Block'
