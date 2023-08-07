from django import forms
from django.core.exceptions import ValidationError
from django.db import models
# Create your models here.
from django.forms.utils import ErrorList
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel, MultiFieldPanel, \
    InlinePanel
from wagtail.core.blocks import StreamBlock, StructBlock, CharBlock, PageChooserBlock, StreamBlockValidationError, \
    URLBlock, BooleanBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Orderable
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.snippets.models import register_snippet

from .blocks.custom_choice_block import CustomChoiceBlock
from .blocks.link_block import LinkBlockStructValue
from .choices import NAV_LINK_TYPE_CHOICES


class MenuLinkBlock(StructBlock):
    link_type = CustomChoiceBlock(label='Type', choices=NAV_LINK_TYPE_CHOICES, default=NAV_LINK_TYPE_CHOICES[0][0],
                                  required=False, widget=forms.RadioSelect)
    link_opens_in_new_tab = BooleanBlock(required=False)
    url = CharBlock(label='URL', required=False)
    page = PageChooserBlock(required=False)
    document = DocumentChooserBlock(required=False)
    anchor = CharBlock(required=False,
                       help_text="This will only work properly if there is an anchor block dropped on the home page")
    link_text = CharBlock(label='Text', required=False)

    # link_format = CustomChoiceBlock(label='Format', choices=LINK_FORMAT_CHOICES, default=LINK_FORMAT_CHOICES[0][0],
    #                                 required=False, widget=forms.RadioSelect)

    def clean(self, value):
        """
        Override to conditionally require the appropriate link field. See admin.js for client-side validation.
        """
        value = super(MenuLinkBlock, self).clean(value)
        values = {f: v for f, v in value.items()}
        link_type = values['link_type']
        errors = {}
        if link_type:
            for field in [link_type, 'link_text']:
                if not values[field]:
                    errors[field] = ErrorList(['This field is required.'])
        if errors:
            raise StreamBlockValidationError(block_errors=errors)
        return value

    class Meta:
        icon = 'fa-link'
        form_classname = 'link-block struct-block'
        value_class = LinkBlockStructValue
        template = 'blocks/navigation_link_block.html'


class SubMenuBlock(MenuLinkBlock):
    pass


class SubMenuStreamBlock(StreamBlock):
    submenu_block = SubMenuBlock()


class MenuStreamBlock(StreamBlock):
    link_block = MenuLinkBlock()

    class Meta:
        min_mum = 1
        max_num = 1


class MenuItem(Orderable):
    menu_link = StreamField(MenuStreamBlock(), blank=True, null=True)
    sub_menu = StreamField(SubMenuStreamBlock(), blank=True, null=True)

    @property
    def main_link(self):
        return self.menu_link.stream_block.child_blocks['link_block']

    page = ParentalKey("Menu", related_name="menu_items", )

    panels = [
        StreamFieldPanel('menu_link'),
        StreamFieldPanel('sub_menu'),
    ]


@register_snippet
class Menu(ClusterableModel):
    """The main menu clusterable model."""

    MENU_CHOICES = (
        ("main-header-menu", 'Main Header Menu'),
        ("main-eyebrow-menu", 'Main Eyebrow Menu'),
        ("footer-extra-menu", 'Footer Extra Menu'),
    )

    title = models.CharField(max_length=30, choices=MENU_CHOICES)

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
        ], heading="Menu"),
        InlinePanel("menu_items", label="Menu Item")
    ]

    def __str__(self):
        return dict(self.MENU_CHOICES)[self.title]


class SocialItem(StructBlock):
    SOCIAL_CHOICES = (
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('instagram', 'Instagram'),
        ('tiktok', 'TikTok'),
        ('youtube', 'YouTube'),
        ('spotify', 'Spotify'),
    )

    icon_class = CustomChoiceBlock(label='Social', choices=SOCIAL_CHOICES, default=SOCIAL_CHOICES[0][0],
                                   widget=forms.RadioSelect)
    link = URLBlock()

    class Meta:
        icon = 'fa-share-square-o'


class SocialsStreamBlock(StreamBlock):
    social_item = SocialItem()


@register_snippet
class Social(ClusterableModel):
    """The main menu clusterable model."""
    socials = StreamField(SocialsStreamBlock(), blank=True, null=True)
    panels = [
        StreamFieldPanel('socials'),
    ]

    def save(self, *args, **kwargs):
        if not self.pk and Social.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one Socials Snippet')
        return super(Social, self).save(**kwargs)
