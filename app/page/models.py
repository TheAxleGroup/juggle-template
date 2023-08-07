from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models

# Create your models here.
from django.forms import CharField
from django.db.models import BooleanField
from django.http import JsonResponse, Http404
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import StreamFieldPanel, TabbedInterface, ObjectList, FieldPanel, MultiFieldPanel, \
    InlinePanel, FieldRowPanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.blocks import StreamBlock
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.search import index
from wagtailmodelchooser import register_model_chooser

from .blocks.collage_hero_block import CollageHeroBlock
from .blocks.hero_block import HeroBlock, StaticHeroBlock
from .blocks.hubspot_form_block import HubspotFormBlock
from .blocks.image_row_block import ImageRowBlock
from .blocks.icon_grid_link_block import IconGridLinkBlock
from .blocks.icon_text_row_block import IconTextRowBlock
from .blocks.image_text_block import ImageTextBlock
from .blocks.internal_hero_block import InternalHeroBlock
from .blocks.multi_column_block import MultiColumnBlock
from .blocks.pattern_hero_block import PatternHeroBlock
from .blocks.plan_block import PlanBlock
from .blocks.quote_block import QuoteBlock
from .blocks.simple_hero_block import SimpleHeroBlock
from .blocks.simple_text_block import SimpleTextBlock
from .blocks.image_grid_text_block import ImageGridTextBlock
from .blocks.slider_hero_block import SliderHeroBlock
from .blocks.three_column_image_link_block import ThreeColumnIconTextBlock
from .views import get_page_meta_data
from wagtailcache.cache import WagtailCacheMixin


class DefaultStreamBlock(StreamBlock):
    three_column_image_link_block = ThreeColumnIconTextBlock()
    square_image_text_block = ImageGridTextBlock()
    simple_text_block = SimpleTextBlock()
    image_text_block = ImageTextBlock()
    multi_column_block = MultiColumnBlock()
    hero_block = HeroBlock()
    static_hero_block = StaticHeroBlock()
    quote_block = QuoteBlock()
    internal_hero_block = InternalHeroBlock()
    hubspot_form_block = HubspotFormBlock()
    plan_block = PlanBlock()


class AbstractBasePage(Page):
    # SEO Metadata Fields
    canonical_url = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name="Canonical URL",
        help_text='Leave this blank unless you know there is a canonical URL for this content.')
    meta_keywords = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name="Meta Keywords")
    exclude_from_sitemap = models.BooleanField(default=False, help_text='Removes this page from sitemap.xml')
    og_title = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name="OG:Title")
    og_type = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name="OG:Type")
    og_url = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name="OG:URL")
    og_image = models.ForeignKey(
        'mediamodels.CustomImage', blank=True, null=True,
        verbose_name="OG:Image",
        related_name="+", on_delete=models.SET_NULL)
    og_description = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name="OG:Description")

    # Meta Tab
    promote_panels = [
        MultiFieldPanel([
            FieldPanel('slug'),
            FieldPanel('canonical_url'),
            FieldPanel('seo_title'),
            FieldPanel('search_description'),
            FieldPanel('meta_keywords'),
            FieldPanel('exclude_from_sitemap'),
        ], heading='Meta Information', classname='collapsible'),
        MultiFieldPanel([
            FieldPanel('og_title'),
            FieldPanel('og_type'),
            FieldPanel('og_url'),
            ImageChooserPanel('og_image'),
            FieldPanel('og_description'),
        ], heading='Open Graph Information', classname='collapsible'),
    ]
    # Add in publish dates
    meta_panels = ObjectList(promote_panels + Page.settings_panels, heading='Meta', classname='settings')

    class Meta:
        abstract = True

    def get_sitemap_urls(self, request=None):
        if not self.exclude_from_sitemap:
            return super().get_sitemap_urls(request=request)
        return []


class DefaultPage(WagtailCacheMixin, AbstractBasePage):
    cache_control = 'public, max-age=3600'

    body = StreamField(DefaultStreamBlock(required=False), blank=True, null=True)
    show_newsletter_form = BooleanField(default=True)

    # Content Tab
    content_panels = AbstractBasePage.content_panels + [
        StreamFieldPanel('body'),
    ]

    # Unused but still causes an error if you remove it
    meta_panels = []

    # Tabs
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        AbstractBasePage.meta_panels,
        ObjectList([FieldPanel('show_newsletter_form')], heading='Page Settings'),
    ])

    search_fields = AbstractBasePage.search_fields + [
        index.SearchField('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context.update(get_page_meta_data(request, self))
        return context

#
# class CampaignPage(WagtailCacheMixin, AbstractBasePage):
#     cache_control = 'public, max-age=3600'
#
#     # body = StreamField(DefaultStreamBlock(required=False), blank=True, null=True)
#
#     fairhill_logo = models.ForeignKey(
#         'mediamodels.CustomImage', blank=True, null=True,
#         related_name="+", on_delete=models.SET_NULL)
#     hero_image = models.ForeignKey(
#         'mediamodels.CustomImage', blank=True, null=True,
#         related_name="+", on_delete=models.SET_NULL)
#     who_we_serve_image = models.ForeignKey(
#         'mediamodels.CustomImage', blank=True, null=True,
#         related_name="+", on_delete=models.SET_NULL)
#     fairhill_experience_image = models.ForeignKey(
#         'mediamodels.CustomImage', blank=True, null=True,
#         related_name="+", on_delete=models.SET_NULL)
#     image_row_1 = models.ForeignKey(
#         'mediamodels.CustomImage', blank=True, null=True,
#         related_name="+", on_delete=models.SET_NULL)
#     image_row_2 = models.ForeignKey(
#         'mediamodels.CustomImage', blank=True, null=True,
#         related_name="+", on_delete=models.SET_NULL)
#     image_row_3 = models.ForeignKey(
#         'mediamodels.CustomImage', blank=True, null=True,
#         related_name="+", on_delete=models.SET_NULL)
#     connect_with_us_image = models.ForeignKey(
#         'mediamodels.CustomImage', blank=True, null=True,
#         related_name="+", on_delete=models.SET_NULL)
#
#
#     # # Content Tab
#     content_panels = AbstractBasePage.content_panels + [
#         ImageChooserPanel('fairhill_logo'),
#         ImageChooserPanel('hero_image'),
#         ImageChooserPanel('who_we_serve_image'),
#         ImageChooserPanel('fairhill_experience_image'),
#         ImageChooserPanel('image_row_1'),
#         ImageChooserPanel('image_row_2'),
#         ImageChooserPanel('image_row_3'),
#         ImageChooserPanel('connect_with_us_image'),
#     ]
#
#     # Unused but still causes an error if you remove it
#     meta_panels = []
#
#     # Tabs
#     edit_handler = TabbedInterface([
#         ObjectList(content_panels, heading='Content'),
#         AbstractBasePage.meta_panels,
#     ])
#
#     # search_fields = AbstractBasePage.search_fields + [
#     #     index.SearchField('body'),
#     # ]
#
#     def get_context(self, request, *args, **kwargs):
#         context = super().get_context(request)
#         context.update(get_page_meta_data(request, self))
#         return context
#
#
# class BlogIndexPage(RoutablePageMixin, DefaultPage):
#     subpage_types = ['BlogPage']
#
#     class Meta:
#         verbose_name = 'Blog Index Page'
#         verbose_name_plural = 'Blog Index Pages'
#
#     @classmethod
#     def get_blog_index_page(cls):
#         return BlogIndexPage.objects.first()
#
#     @classmethod
#     def can_create_at(cls, parent):
#         # Only allow one child instance
#         return super(BlogIndexPage, cls).can_create_at(parent) and not cls.objects.exists()
#
#     @route(r'^$')
#     def blog_list(self, request, year=None, month=None, day=None, *args, **kwargs):
#         blogs = BlogPage.objects.live().order_by('-last_published_at')
#
#         # # Handle date filter
#         # self.filter_date = None
#         # if year:
#         #     blogs = blogs.filter(date__year=year)
#         #     self.filter_date = datetime.datetime.today().replace(year=int(year), month=1, day=1)
#         # if month:
#         #     blogs = blogs.filter(date__month=month)
#         #     self.filter_date = self.filter_date.replace(month=int(month))
#         # if day:
#         #     blogs = blogs.filter(date__day=day)
#         #     self.filter_date = self.filter_date.replace(day=int(day))
#
#         # Handle pagination
#         paginator = Paginator(blogs, 6)
#         try:
#             self.blogs = paginator.page(request.GET.get('page'))  # Return linked page
#         except PageNotAnInteger:
#             self.blogs = paginator.page(1)  # Return first page
#         except EmptyPage:
#             self.blogs = paginator.page(paginator.num_pages)  # Return last page
#
#         return Page.serve(self, request, *args, **kwargs)
#
#     @route(r'^(.+)/$')
#     def blog_page_detail(self, request, slug, *args, **kwargs):
#         try:
#             page = BlogPage.objects.get(slug=slug)
#         except BlogPage.DoesNotExist:
#             raise Http404
#
#         page.additional_breadcrumbs = [({'title': page.title, 'url': page.get_url()})]
#         return Page.serve(page, request, *args, **kwargs)
#
#     content_panels = DefaultPage.content_panels
#
#     edit_handler = TabbedInterface([
#         ObjectList(content_panels, heading='Content'),
#         AbstractBasePage.meta_panels,
#     ])
#
#
# @register_model_chooser
# class BlogPage(RoutablePageMixin, DefaultPage):
#     cover_image = models.ForeignKey(
#         'mediamodels.CustomImage', models.SET_NULL, null=True,
#         help_text='Logo used for featured block',
#         related_name='cover_image')
#
#     content_panels = [
#         MultiFieldPanel([
#             ImageChooserPanel('cover_image'),
#         ], heading='Cover Image', classname='collapsible'),
#     ] + DefaultPage.content_panels
#
#     edit_handler = TabbedInterface([
#         ObjectList(content_panels, heading='Content'),
#         AbstractBasePage.meta_panels,
#     ])
#
#     parent_page_types = ['BlogIndexPage']
#     subpage_types = []
#
#     @route(r'^$')
#     def redirect_to_detail_view(self, request, *args, **kwargs):
#         return redirect(self.get_url())
#
#     @property
#     def get_blog_index_page(self):
#         return self.get_parent().get_url()
#
#     def get_url(self):
#         return '{}{}/'.format(self.get_blog_index_page, self.slug)
#
#     def get_full_url(self, request=None):
#         url_parts = self.get_url_parts(request=request)
#         site_id, root_url, page_path = url_parts
#         return root_url + self.get_url()
#
#     def get_next(self):
#         if self.get_next_sibling():
#             return self.get_next_sibling().specific
#         else:
#             return self.get_siblings().first().specific
#
#     def get_prev(self):
#         if self.get_prev_sibling():
#             return self.get_prev_sibling().specific
#         else:
#             return self.get_siblings().last().specific
#


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    thank_you_text = RichTextField()
    button_text = models.CharField(max_length=255, default='Send')

    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        FieldPanel('button_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def get_sitemap_urls(self, request=None):
        return []

    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form(request.POST, request.FILES, page=self, user=request.user)

            if form.is_valid():
                form_submission = self.process_form_submission(form)
                return JsonResponse({'submission': '200'})
            return JsonResponse({'submission': 'err'})
        else:
            form = self.get_form(page=self, user=request.user)

            context = self.get_context(request)
            context['form'] = form
            return TemplateResponse(
                request,
                self.get_template(request),
                context
            )
