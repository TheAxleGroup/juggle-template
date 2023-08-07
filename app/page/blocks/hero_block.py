from wagtail.core.blocks import CharBlock, StructBlock, RichTextBlock, StreamBlock, BooleanBlock
from wagtail.images.blocks import ImageChooserBlock

from ..blocks.link_block import LinkBlock


class HeroSlide(StructBlock):
    header = CharBlock(required=False)
    subheader = RichTextBlock()
    desktop_image = ImageChooserBlock()
    mobile_image = ImageChooserBlock(required=False)

    class Meta:
        label = 'Hero Slide'
        icon = 'image'


class HeroSlideStreamBlock(StreamBlock):
    hero_slide = HeroSlide()

    class Meta:
        min_num = 2


class HeroBlock(StructBlock):
    super_header = CharBlock(required=False)
    button_link = LinkBlock()
    hero_slides = HeroSlideStreamBlock()

    class Meta:
        template = 'blocks/hero_block.html'
        label = 'Slider Hero Block'
        icon = 'image'


class AppLink(StructBlock):
    app_link_image = ImageChooserBlock()
    app_link_url = CharBlock()

    class Meta:
        label = 'App Link'
        icon = 'image'


class AppLinkStreamBlock(StreamBlock):
    app_link = AppLink()

    class Meta:
        max_num = 2


class StaticHeroBlock(StructBlock):
    header = RichTextBlock(required=False)
    colored_words = CharBlock(required=False)
    colored_words_size = BooleanBlock(required=False, help_text="Increase the size of the blue colored words")
    subheader = RichTextBlock(required=False)
    desktop_image = ImageChooserBlock()
    mobile_image = ImageChooserBlock(required=False)
    button_link = LinkBlock()
    app_links = AppLinkStreamBlock(required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        size = bool(context['self']['colored_words_size'])
        s1 = str(context['self']['header'])
        s2 = str(context['self']['colored_words'])
        s2 = s2.split(' ')
        if size:
            for word in s2:
                s1 = s1.replace(word, '<span class="text-secondary font-semibold text-54">{}</span>'.format(word))
                context['self']['header'] = s1
            return context
        else:
            for word in s2:
                s1 = s1.replace(word, '<span class="text-secondary font-semibold">{}</span>'.format(word))
                context['self']['header'] = s1
            return context

    class Meta:
        template = 'blocks/static_hero_block.html'
        label = 'Static Hero Block'
        icon = 'image'
