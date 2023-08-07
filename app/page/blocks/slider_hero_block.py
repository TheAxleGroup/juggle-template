from wagtail.core.blocks import CharBlock, StructBlock, RichTextBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock

from ..blocks.link_block import LinkBlock


class HeroSlide(StructBlock):
    header = CharBlock(required=False)
    subheader = RichTextBlock()
    desktop_image = ImageChooserBlock()
    mobile_image = ImageChooserBlock(required=False)
    button_link = LinkBlock()

    class Meta:
        label = 'Hero Slide'
        icon = 'image'


class HeroSlideStreamBlock(StreamBlock):
    hero_slide = HeroSlide()

    class Meta:
        min_num = 2
        max_num = 4


class Statistic(StructBlock):
    statistic = CharBlock()
    statistic_description = CharBlock()

    class Meta:
        icon = 'percent'


class StatisticStreamBlock(StreamBlock):
    statistic_item = Statistic()

    class Meta:
        required = False
        icon = 'percent'
        max_num = 3


class HeroSubInfoBlock(StructBlock):
    header = CharBlock(required=False)
    content = RichTextBlock(required=False)
    button_link = LinkBlock()
    statistics = StatisticStreamBlock()

    class Meta:
        required = False


class SliderHeroBlock(StructBlock):
    hero_slides = HeroSlideStreamBlock()
    sub_block = HeroSubInfoBlock()

    class Meta:
        template = 'blocks/slider_hero_block.html'
        label = 'Slider Hero Block'
        icon = 'images'
