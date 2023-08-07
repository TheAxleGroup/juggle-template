# Insert sitewide admin JS
from django import forms
from django.db import models
from wagtail.admin.edit_handlers import PageChooserPanel, MultiFieldPanel, FieldPanel, TabbedInterface, ObjectList
from wagtail.contrib.frontend_cache.utils import PurgeBatch
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.core import hooks
from django.templatetags.static import static
from django.utils.html import format_html
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailcache.cache import clear_cache

from .models import DefaultPage


@hooks.register('insert_global_admin_js')
def global_admin_js():
    # Returns HTML/Javascript to the admin template
    scripts = ''

    scripts += format_html('<script src="{}"></script>', static('js/admin.js'))
    return scripts


@register_setting(icon='cogs')
class GTMSettings(BaseSetting):
    class Meta:
        verbose_name = 'GTM Settings'

    gtm_header_code = models.CharField(
        null=True, blank=True, default='',
        max_length=1024,
        verbose_name='GTM Header Code',
        help_text='The code that goes high as possible in the <head> tag',
    )

    gtm_body_code = models.CharField(
        null=True, blank=True, default='',
        max_length=1024,
        verbose_name='GTM Body Code',
        help_text='The code that goes right after opening the <body> tag',
    )

    panels = [
        FieldPanel('gtm_header_code', widget=forms.Textarea),
        FieldPanel('gtm_body_code', widget=forms.Textarea),
    ]


@register_setting(icon='cogs')
class HeaderFooter(BaseSetting):
    class Meta:
        verbose_name = 'Header & Footer'

    # General
    header_logo = models.ForeignKey(
        'mediamodels.CustomImage', models.SET_NULL, blank=True, null=True,
        help_text='Logo used in header. Recommended transparent PNG',
        related_name='header_logo')
    footer_logo = models.ForeignKey(
        'mediamodels.CustomImage', models.SET_NULL, blank=True, null=True,
        help_text='Logo used in footer. Recommended transparent PNG',
        related_name='footer_logo')

    footer_background = models.ForeignKey(
        'mediamodels.CustomImage', models.SET_NULL, blank=True, null=True,
        help_text='Background design for the footer',
        related_name='footer_background')

    footer_form_text = models.CharField(
        null=True, blank=True, default='',
        max_length=512,
        verbose_name='Footer contact text',
        help_text='The text that shows above the footer contact button.')
    footer_copyright_text = models.CharField(
        null=True, blank=True, default='',
        max_length=512,
        verbose_name='Footer copyright text',
        help_text='Enter the text that should appear after the year in the copyright line.')

    footer_contact_form = models.TextField(verbose_name='Footer HS Form', null=True, blank=True, default='')

    footer_form_header = models.CharField(
        null=True, blank=True, default='',
        max_length=512)

    footer_address_1 = models.CharField(
        null=True, blank=True, default='',
        max_length=512)

    footer_address_2 = models.CharField(
        null=True, blank=True, default='',
        max_length=512)

    footer_address_3 = models.CharField(
        null=True, blank=True, default='',
        max_length=512)

    general_tab_panels = [
        MultiFieldPanel([
            ImageChooserPanel('header_logo'),
            ImageChooserPanel('footer_logo'),
        ], heading='Logos', classname='collapsible'),
    ]

    footer_tab_panels = [
        MultiFieldPanel([
            FieldPanel('footer_copyright_text'),
            FieldPanel('footer_form_text'),
            FieldPanel('footer_form_header'),
            FieldPanel('footer_contact_form'),
            FieldPanel('footer_address_1'),
            FieldPanel('footer_address_2'),
            FieldPanel('footer_address_3'),
            ImageChooserPanel('footer_background'),

        ], heading='Footer', classname='collapsible'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(general_tab_panels, heading='General'),
        ObjectList(footer_tab_panels, heading='Footer'),
    ])


@hooks.register('after_create_page')
@hooks.register('after_edit_page')
@hooks.register('after_publish_page')
def clear_wagtailcache(request, page):
    batch = PurgeBatch()
    batch.add_pages(DefaultPage.objects.all())
    batch.purge()

    if page.live:
        clear_cache()


@hooks.register("register_icons")
def register_icons(icons):
    return icons + [
        'wagtailfontawesomesvg/solid/font.svg',
        'wagtailfontawesomesvg/solid/image.svg',
        'wagtailfontawesomesvg/solid/images.svg',
        'wagtailfontawesomesvg/solid/link.svg',
        'wagtailfontawesomesvg/solid/th.svg',
        'wagtailfontawesomesvg/solid/circle.svg',
        'wagtailfontawesomesvg/solid/square.svg',
        'wagtailfontawesomesvg/solid/arrows-alt-h.svg',
        'wagtailfontawesomesvg/solid/align-justify.svg',
        'wagtailfontawesomesvg/solid/columns.svg',
        'wagtailfontawesomesvg/solid/video.svg',
        'wagtailfontawesomesvg/solid/window-maximize.svg',
        'wagtailfontawesomesvg/solid/quote-left.svg',
        'wagtailfontawesomesvg/solid/percent.svg',
        'wagtailfontawesomesvg/solid/border-all.svg',
        'wagtailfontawesomesvg/solid/map.svg',
    ]
