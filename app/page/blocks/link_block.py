from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from wagtail.core.blocks import StructValue, StructBlock, CharBlock, PageChooserBlock, EmailBlock, \
    StreamBlockValidationError, BooleanBlock
from wagtail.documents.blocks import DocumentChooserBlock
from django import forms

from .custom_choice_block import CustomChoiceBlock
from ..choices import LINK_TYPE_CHOICES, REQUIRED_LINK_TYPE_CHOICES


class LinkBlockStructValue(StructValue):
    def href(self):
        """
        Return extra values to the template context.
        """
        link_type = self.get('link_type')
        href = self.get(link_type)
        if link_type == 'page':
            return self.get('page').get_url()
        if link_type == 'document':
            return href.file.url
        return href

    def href_prefix(self):
        """
        Return extra values to the template context.
        """
        link_type = self.get('link_type')
        prefix = ''
        if link_type == 'phone':
            prefix = 'tel:'
        if link_type == 'email':
            prefix = 'mailto:'
        if link_type == 'anchor':
            prefix = '#'
        return prefix

    def full_href(self):
        return self.href_prefix() + self.href()


BUTTON_STYLE_CHOICES = (
    (' btn-link ', 'Link Style'),
    (' btn-primary ', 'Button Style'),
)


class LinkBlock(StructBlock):
    link_type = CustomChoiceBlock(label='Type', choices=LINK_TYPE_CHOICES, default=LINK_TYPE_CHOICES[0][0],
                                  required=False, widget=forms.RadioSelect)
    link_opens_in_new_tab = BooleanBlock(required=False)
    url = CharBlock(label='URL', required=False)
    page = PageChooserBlock(required=False)
    document = DocumentChooserBlock(required=False)
    email = EmailBlock(required=False)
    phone = CharBlock(required=False)
    anchor = CharBlock(required=False,
                       help_text="This will only work properly if there is an anchor block dropped on the home page")
    link_text = CharBlock(label='Text', required=False)

    # link_format = CustomChoiceBlock(label='Format', choices=LINK_FORMAT_CHOICES, default=LINK_FORMAT_CHOICES[0][0],
    #                                 required=False, widget=forms.RadioSelect)

    def clean(self, value):
        """
        Override to conditionally require the appropriate link field. See admin.js for client-side validation.
        """
        value = super(LinkBlock, self).clean(value)
        values = {f: v for f, v in value.items()}
        link_type = values['link_type']
        errors = {}

        if link_type:
            for field in [link_type, 'link_text']:
                if not values[field] or values[field] == '':
                    errors[field] = ErrorList(['This field is required.'])

        if errors:
            raise ValidationError("Link block error", params=errors)

        return value

    class Meta:
        icon = 'link'
        value_class = LinkBlockStructValue
        form_classname = 'link-block struct-block'
        template = 'blocks/partials/link_block_partial.html'


class RequiredLinkBlock(LinkBlock):
    link_type = CustomChoiceBlock(label='Type', choices=REQUIRED_LINK_TYPE_CHOICES, default=REQUIRED_LINK_TYPE_CHOICES[0][0],
                                  required=False, widget=forms.RadioSelect)


class StyleLinkBlock(LinkBlock):
    button_style = CustomChoiceBlock(label='Button Style', choices=BUTTON_STYLE_CHOICES,
                                     default=BUTTON_STYLE_CHOICES[1][0],
                                     required=False, widget=forms.Select)
