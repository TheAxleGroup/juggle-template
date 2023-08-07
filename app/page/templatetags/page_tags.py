from django import template
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from taggit.models import Tag
from wagtail.core.models import Site

from ..snippets import Menu, Social
from ..wagtail_hooks import HeaderFooter

register = template.Library()


@register.simple_tag(takes_context=True)
def get_header_menu(context):
    return Menu.objects.filter(title='main-header-menu').first()


@register.simple_tag(takes_context=True)
def get_menu(context, slug):
    request = context['request']
    return Menu.objects.filter(title=slug).first()


@register.simple_tag(takes_context=True)
def get_menu_last(context):
    request = context['request']
    if Site.find_for_request(request).is_default_site:
        return Menu.objects.filter(title='main-header-menu').first().menu_items.last()
    else:
        return Menu.objects.filter(title='careers-header-menu').first().menu_items.last()


@register.simple_tag
def get_small_footer_menu():
    return Menu.objects.filter(title='footer-extra-menu').first()


@register.simple_tag
def get_menu_for_site(site):
    return Menu.objects.filter(title='main-header-menu').first()


@register.simple_tag
def get_socials():
    if not Social.objects.first():
        return None

    return Social.objects.first().socials


@register.simple_tag
def defer_css(href):
    ret = ('<link rel="preload" href="%s" as="style" onload="this.onload=null;this.rel=\'stylesheet\'"/>'
           '<noscript>'
           '<link href="%s" rel="stylesheet">'
           '</noscript>'
           ) % (href, href)
    return mark_safe(ret)


@register.simple_tag
def reformat_table(table):
    table = table['data']
    buckets = table[0][1:]
    reformat = {key: [] for key in buckets}

    for entry in table[1:]:
        for i, data in enumerate(entry[1:]):
            reformat[buckets[i]].append([entry[0], data])

    return reformat


@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    """
    Returns the URL-encoded querystring for the current page,
    updating the params with the key/value pairs passed to the tag.
    Also removes pipe-delimited params within _remove

    E.g: given the querystring ?foo=1&bar=2
    {% query_transform bar=3 %} outputs ?foo=1&bar=3
    {% query_transform foo='baz' %} outputs ?foo=baz&bar=2
    {% query_transform foo='one' _remove='bar|baz' %} outputs ?foo=one

    A RequestContext is required for access to the current querystring.
    """
    query = context['request'].GET.copy()
    remove = []
    for k, v in kwargs.items():
        if k == '_remove':
            remove = v.split('|')
        else:
            query[k] = v
    for k in remove:
        query.pop(k, None)
    return query.urlencode()


@register.simple_tag
def _dir(val):
    print(dir(val))


@register.simple_tag(takes_context=True)
def get_form_data(context, form_page):
    request = context['request']

    form = form_page.get_form(
        page=form_page, user=request.user)

    return {'page': form_page, 'form': form}


@register.simple_tag(takes_context=True)
def get_footer_form(context):
    request = context['request']
    form_settings = HeaderFooter.for_site(Site.find_for_request(request))

    if form_settings.footer_contact_form is None:
        return None

    form_page = form_settings.footer_contact_form.specific

    form = form_page.get_form(
        page=form_page, user=request.user)
    return {'page': form_page, 'form': form}


@register.simple_tag(takes_context=True)
def get_sites():
    return Site.objects.all()


@register.filter(is_safe=False)
def multiply(value, arg):
    """Multiply the arg to the value."""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        try:
            return value * arg
        except Exception:
            return ''
