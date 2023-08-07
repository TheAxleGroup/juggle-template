# Generated by Django 3.2.16 on 2023-01-09 17:52

from django.db import migrations
import django.forms.widgets
import page.blocks.custom_choice_block
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailgeowidget.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0036_alter_defaultpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultpage',
            name='body',
            field=wagtail.core.fields.StreamField([('three_column_image_link_block', wagtail.core.blocks.StructBlock([('block_id', wagtail.core.blocks.CharBlock(required=False)), ('block_header', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('button_style', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' btn-link ', 'Link Style'), (' btn-primary ', 'Button Style')), default=' btn-primary ', label='Button Style', required=False, widget=django.forms.widgets.Select)), ('link_type', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('', 'None'), ('url', 'URL'), ('page', 'Page'), ('document', 'Document'), ('email', 'Email'), ('anchor', 'Anchor'), ('phone', 'Phone')), default='', label='Type', required=False, widget=django.forms.widgets.RadioSelect)), ('link_opens_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(label='URL', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('email', wagtail.core.blocks.EmailBlock(required=False)), ('phone', wagtail.core.blocks.CharBlock(required=False)), ('anchor', wagtail.core.blocks.CharBlock(help_text='This will only work properly if there is an anchor block dropped on the home page', required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Text', required=False))])), ('image_links', wagtail.core.blocks.StreamBlock([('image_link_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('block_title', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.StructBlock([('button_style', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' btn-link ', 'Link Style'), (' btn-primary ', 'Button Style')), default=' btn-primary ', label='Button Style', required=False, widget=django.forms.widgets.Select)), ('link_type', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('url', 'URL'), ('page', 'Page'), ('document', 'Document'), ('email', 'Email'), ('anchor', 'Anchor'), ('phone', 'Phone')), default='url', label='Type', required=False, widget=django.forms.widgets.RadioSelect)), ('link_opens_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(label='URL', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('email', wagtail.core.blocks.EmailBlock(required=False)), ('phone', wagtail.core.blocks.CharBlock(required=False)), ('anchor', wagtail.core.blocks.CharBlock(help_text='This will only work properly if there is an anchor block dropped on the home page', required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Text', required=False))]))]))]))])), ('square_image_text_block', wagtail.core.blocks.StructBlock([('block_id', wagtail.core.blocks.CharBlock(required=False)), ('image_order', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('left', 'Images First'), ('right', 'Text First')), default='left', label='Column Order', required=False, widget=django.forms.widgets.RadioSelect)), ('images', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('text_column', wagtail.core.blocks.StructBlock([('list_style', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('', 'Dashed list'), ('check-style', 'Check mark list'), ('x-style', 'X list')), default='', label='List Style', required=False, widget=django.forms.widgets.Select)), ('text_header', wagtail.core.blocks.CharBlock(required=False)), ('text_content', wagtail.core.blocks.RichTextBlock()), ('button_link', wagtail.core.blocks.StructBlock([('button_style', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' btn-link ', 'Link Style'), (' btn-primary ', 'Button Style')), default=' btn-primary ', label='Button Style', required=False, widget=django.forms.widgets.Select)), ('link_type', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('', 'None'), ('url', 'URL'), ('page', 'Page'), ('document', 'Document'), ('email', 'Email'), ('anchor', 'Anchor'), ('phone', 'Phone')), default='', label='Type', required=False, widget=django.forms.widgets.RadioSelect)), ('link_opens_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(label='URL', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('email', wagtail.core.blocks.EmailBlock(required=False)), ('phone', wagtail.core.blocks.CharBlock(required=False)), ('anchor', wagtail.core.blocks.CharBlock(help_text='This will only work properly if there is an anchor block dropped on the home page', required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Text', required=False))]))]))])), ('simple_text_block', wagtail.core.blocks.StructBlock([('block_id', wagtail.core.blocks.CharBlock(required=False)), ('image_background', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_column', wagtail.core.blocks.StructBlock([('column_width', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' col-span-2 ', '2/12 Width'), (' col-span-3 ', '3/12 Width'), (' col-span-4 ', '4/12 Width'), (' col-span-5 ', '5/12 Width'), (' col-span-6 ', '6/12 Width'), (' col-span-7 ', '7/12 Width'), (' col-span-8 ', '8/12 Width'), (' col-span-9 ', '9/12 Width'), (' col-span-10 ', '10/12 Width'), (' col-span-11 ', '11/12 Width'), (' col-span-12 ', '12/12 Width')), default=' col-span-4 ', label='Column Width', required=False, widget=django.forms.widgets.Select)), ('list_style', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('', 'Dashed list'), ('check-style', 'Check mark list'), ('x-style', 'X list')), default='', label='List Style', required=False, widget=django.forms.widgets.Select)), ('text_header', wagtail.core.blocks.CharBlock(required=False)), ('text_content', wagtail.core.blocks.RichTextBlock())])), ('link_cards', wagtail.core.blocks.StreamBlock([('card', wagtail.core.blocks.StructBlock([('card_content', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.StructBlock([('button_style', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' btn-link ', 'Link Style'), (' btn-primary ', 'Button Style')), default=' btn-primary ', label='Button Style', required=False, widget=django.forms.widgets.Select)), ('link_type', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('url', 'URL'), ('page', 'Page'), ('document', 'Document'), ('email', 'Email'), ('anchor', 'Anchor'), ('phone', 'Phone')), default='url', label='Type', required=False, widget=django.forms.widgets.RadioSelect)), ('link_opens_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(label='URL', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('email', wagtail.core.blocks.EmailBlock(required=False)), ('phone', wagtail.core.blocks.CharBlock(required=False)), ('anchor', wagtail.core.blocks.CharBlock(help_text='This will only work properly if there is an anchor block dropped on the home page', required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Text', required=False))]))]))])), ('square_images', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('button_link', wagtail.core.blocks.StructBlock([('button_style', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' btn-link ', 'Link Style'), (' btn-primary ', 'Button Style')), default=' btn-primary ', label='Button Style', required=False, widget=django.forms.widgets.Select)), ('link_type', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('', 'None'), ('url', 'URL'), ('page', 'Page'), ('document', 'Document'), ('email', 'Email'), ('anchor', 'Anchor'), ('phone', 'Phone')), default='', label='Type', required=False, widget=django.forms.widgets.RadioSelect)), ('link_opens_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(label='URL', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('email', wagtail.core.blocks.EmailBlock(required=False)), ('phone', wagtail.core.blocks.CharBlock(required=False)), ('anchor', wagtail.core.blocks.CharBlock(help_text='This will only work properly if there is an anchor block dropped on the home page', required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Text', required=False))]))])), ('image_text_block', wagtail.core.blocks.StructBlock([('block_id', wagtail.core.blocks.CharBlock(required=False)), ('image_order', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('left', 'Desktop Image First'), ('right', 'Desktop Text First')), default='left', label='Desktop Column Order', required=False, widget=django.forms.widgets.RadioSelect)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('crop_image_to_match_height', wagtail.core.blocks.BooleanBlock(help_text='Crops the image so that it is equal height with the text column.', required=False)), ('text_column', wagtail.core.blocks.StructBlock([('list_style', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('', 'Dashed list'), ('check-style', 'Check mark list'), ('x-style', 'X list')), default='', label='List Style', required=False, widget=django.forms.widgets.Select)), ('text_header', wagtail.core.blocks.CharBlock(required=False)), ('text_content', wagtail.core.blocks.RichTextBlock()), ('button_link', wagtail.core.blocks.StructBlock([('button_style', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' btn-link ', 'Link Style'), (' btn-primary ', 'Button Style')), default=' btn-primary ', label='Button Style', required=False, widget=django.forms.widgets.Select)), ('link_type', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('', 'None'), ('url', 'URL'), ('page', 'Page'), ('document', 'Document'), ('email', 'Email'), ('anchor', 'Anchor'), ('phone', 'Phone')), default='', label='Type', required=False, widget=django.forms.widgets.RadioSelect)), ('link_opens_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(label='URL', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('email', wagtail.core.blocks.EmailBlock(required=False)), ('phone', wagtail.core.blocks.CharBlock(required=False)), ('anchor', wagtail.core.blocks.CharBlock(help_text='This will only work properly if there is an anchor block dropped on the home page', required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Text', required=False))]))])), ('custom_list', wagtail.core.blocks.StreamBlock([('bullet_item', wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock())]))]))])), ('multi_column_block', wagtail.core.blocks.StructBlock([('block_id', wagtail.core.blocks.CharBlock(required=False)), ('column_gap', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('gap-x-2', 'Small'), ('gap-x-4', 'Medium'), ('gap-x-8', 'Large'), ('gap-x-12', 'Extra Large')), default='gap-x-8', label='Column Gap', required=False, widget=django.forms.widgets.Select)), ('bg_color', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('', 'Off White Background'), (' bg-gray-1 ', 'Light Gray Background')), default='', label='Background Color', required=False, widget=django.forms.widgets.Select)), ('block_link', wagtail.core.blocks.StructBlock([('button_style', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' btn-link ', 'Link Style'), (' btn-primary ', 'Button Style')), default=' btn-primary ', label='Button Style', required=False, widget=django.forms.widgets.Select)), ('link_type', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('', 'None'), ('url', 'URL'), ('page', 'Page'), ('document', 'Document'), ('email', 'Email'), ('anchor', 'Anchor'), ('phone', 'Phone')), default='', label='Type', required=False, widget=django.forms.widgets.RadioSelect)), ('link_opens_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(label='URL', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('email', wagtail.core.blocks.EmailBlock(required=False)), ('phone', wagtail.core.blocks.CharBlock(required=False)), ('anchor', wagtail.core.blocks.CharBlock(help_text='This will only work properly if there is an anchor block dropped on the home page', required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Text', required=False))])), ('block_header', wagtail.core.blocks.CharBlock(required=False)), ('columns', wagtail.core.blocks.StreamBlock([('image_column', wagtail.core.blocks.StructBlock([('force_column_to_new_row', wagtail.core.blocks.BooleanBlock(required=False)), ('column_width', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' col-span-2 ', '2/12 Width'), (' col-span-3 ', '3/12 Width'), (' col-span-4 ', '4/12 Width'), (' col-span-5 ', '5/12 Width'), (' col-span-6 ', '6/12 Width'), (' col-span-7 ', '7/12 Width'), (' col-span-8 ', '8/12 Width'), (' col-span-9 ', '9/12 Width'), (' col-span-10 ', '10/12 Width'), (' col-span-11 ', '11/12 Width'), (' col-span-12 ', '12/12 Width')), default=' col-span-4 ', label='Column Width', required=False, widget=django.forms.widgets.Select)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('circle_image', wagtail.core.blocks.BooleanBlock(required=False)), ('crop_image_to_match_height', wagtail.core.blocks.BooleanBlock(help_text='Crops the image so that it is equal height with the text column.', required=False))])), ('text_column', wagtail.core.blocks.StructBlock([('force_column_to_new_row', wagtail.core.blocks.BooleanBlock(required=False)), ('text_column', wagtail.core.blocks.StructBlock([('column_width', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' col-span-2 ', '2/12 Width'), (' col-span-3 ', '3/12 Width'), (' col-span-4 ', '4/12 Width'), (' col-span-5 ', '5/12 Width'), (' col-span-6 ', '6/12 Width'), (' col-span-7 ', '7/12 Width'), (' col-span-8 ', '8/12 Width'), (' col-span-9 ', '9/12 Width'), (' col-span-10 ', '10/12 Width'), (' col-span-11 ', '11/12 Width'), (' col-span-12 ', '12/12 Width')), default=' col-span-4 ', label='Column Width', required=False, widget=django.forms.widgets.Select)), ('list_style', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('', 'Dashed list'), ('check-style', 'Check mark list'), ('x-style', 'X list')), default='', label='List Style', required=False, widget=django.forms.widgets.Select)), ('text_header', wagtail.core.blocks.CharBlock(required=False)), ('text_subheader', wagtail.core.blocks.CharBlock(label='Text sub header', required=False)), ('text_content', wagtail.core.blocks.RichTextBlock()), ('button_link', wagtail.core.blocks.StructBlock([('button_style', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' btn-link ', 'Link Style'), (' btn-primary ', 'Button Style')), default=' btn-primary ', label='Button Style', required=False, widget=django.forms.widgets.Select)), ('link_type', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('', 'None'), ('url', 'URL'), ('page', 'Page'), ('document', 'Document'), ('email', 'Email'), ('anchor', 'Anchor'), ('phone', 'Phone')), default='', label='Type', required=False, widget=django.forms.widgets.RadioSelect)), ('link_opens_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(label='URL', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('email', wagtail.core.blocks.EmailBlock(required=False)), ('phone', wagtail.core.blocks.CharBlock(required=False)), ('anchor', wagtail.core.blocks.CharBlock(help_text='This will only work properly if there is an anchor block dropped on the home page', required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Text', required=False))]))]))])), ('icon_content_column', wagtail.core.blocks.StructBlock([('force_column_to_new_row', wagtail.core.blocks.BooleanBlock(required=False)), ('column_width', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' col-span-2 ', '2/12 Width'), (' col-span-3 ', '3/12 Width'), (' col-span-4 ', '4/12 Width'), (' col-span-5 ', '5/12 Width'), (' col-span-6 ', '6/12 Width'), (' col-span-7 ', '7/12 Width'), (' col-span-8 ', '8/12 Width'), (' col-span-9 ', '9/12 Width'), (' col-span-10 ', '10/12 Width'), (' col-span-11 ', '11/12 Width'), (' col-span-12 ', '12/12 Width')), default=' col-span-4 ', label='Column Width', required=False, widget=django.forms.widgets.Select)), ('icons', wagtail.core.blocks.StreamBlock([('icon_content', wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('icon_position', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('top', 'Top Icon'), ('side', 'Side Icon')), default='side', label='Icon Position', required=True, widget=django.forms.widgets.Select)), ('icon_size', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' h-9 w-9 ', 'Regular'), (' h-20 w-20 ', 'Large')), default=' h-9 w-9 ', label='Icon Size', required=True, widget=django.forms.widgets.Select)), ('header', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False))]))]))])), ('embed_column', wagtail.core.blocks.StructBlock([('force_column_to_new_row', wagtail.core.blocks.BooleanBlock(required=False)), ('column_width', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' col-span-2 ', '2/12 Width'), (' col-span-3 ', '3/12 Width'), (' col-span-4 ', '4/12 Width'), (' col-span-5 ', '5/12 Width'), (' col-span-6 ', '6/12 Width'), (' col-span-7 ', '7/12 Width'), (' col-span-8 ', '8/12 Width'), (' col-span-9 ', '9/12 Width'), (' col-span-10 ', '10/12 Width'), (' col-span-11 ', '11/12 Width'), (' col-span-12 ', '12/12 Width')), default=' col-span-4 ', label='Column Width', required=False, widget=django.forms.widgets.Select)), ('embed_link', wagtail.embeds.blocks.EmbedBlock()), ('embed_aspect_ratio', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('56.25%', '16:9'), ('75%', '4:3'), ('66.66%', '3:2')), default='66.66%', label='Embed Aspect Ratio', required=False, widget=django.forms.widgets.Select))])), ('icon_card_column', wagtail.core.blocks.StructBlock([('force_column_to_new_row', wagtail.core.blocks.BooleanBlock(required=False)), ('column_width', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' col-span-2 ', '2/12 Width'), (' col-span-3 ', '3/12 Width'), (' col-span-4 ', '4/12 Width'), (' col-span-5 ', '5/12 Width'), (' col-span-6 ', '6/12 Width'), (' col-span-7 ', '7/12 Width'), (' col-span-8 ', '8/12 Width'), (' col-span-9 ', '9/12 Width'), (' col-span-10 ', '10/12 Width'), (' col-span-11 ', '11/12 Width'), (' col-span-12 ', '12/12 Width')), default=' col-span-4 ', label='Column Width', required=False, widget=django.forms.widgets.Select)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('card_header', wagtail.core.blocks.CharBlock()), ('card_content', wagtail.core.blocks.RichTextBlock()), ('button_link', wagtail.core.blocks.StructBlock([('button_style', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' btn-link ', 'Link Style'), (' btn-primary ', 'Button Style')), default=' btn-primary ', label='Button Style', required=False, widget=django.forms.widgets.Select)), ('link_type', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('', 'None'), ('url', 'URL'), ('page', 'Page'), ('document', 'Document'), ('email', 'Email'), ('anchor', 'Anchor'), ('phone', 'Phone')), default='', label='Type', required=False, widget=django.forms.widgets.RadioSelect)), ('link_opens_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(label='URL', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('email', wagtail.core.blocks.EmailBlock(required=False)), ('phone', wagtail.core.blocks.CharBlock(required=False)), ('anchor', wagtail.core.blocks.CharBlock(help_text='This will only work properly if there is an anchor block dropped on the home page', required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Text', required=False))]))])), ('form_column', wagtail.core.blocks.StructBlock([('force_column_to_new_row', wagtail.core.blocks.BooleanBlock(required=False)), ('column_width', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' col-span-2 ', '2/12 Width'), (' col-span-3 ', '3/12 Width'), (' col-span-4 ', '4/12 Width'), (' col-span-5 ', '5/12 Width'), (' col-span-6 ', '6/12 Width'), (' col-span-7 ', '7/12 Width'), (' col-span-8 ', '8/12 Width'), (' col-span-9 ', '9/12 Width'), (' col-span-10 ', '10/12 Width'), (' col-span-11 ', '11/12 Width'), (' col-span-12 ', '12/12 Width')), default=' col-span-4 ', label='Column Width', required=False, widget=django.forms.widgets.Select)), ('form', wagtail.core.blocks.PageChooserBlock('page.FormPage'))]))]))])), ('form_map_block', wagtail.core.blocks.StructBlock([('block_id', wagtail.core.blocks.CharBlock(required=False)), ('form_header', wagtail.core.blocks.CharBlock()), ('form_subheader', wagtail.core.blocks.CharBlock(required=False)), ('form', wagtail.core.blocks.PageChooserBlock('page.FormPage')), ('location_header', wagtail.core.blocks.CharBlock()), ('location_subheader', wagtail.core.blocks.CharBlock(required=False)), ('maps', wagtail.core.blocks.StreamBlock([('map_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('phone', wagtail.core.blocks.CharBlock(required=False)), ('fax', wagtail.core.blocks.CharBlock(required=False)), ('address', wagtailgeowidget.blocks.GeoAddressBlock(geocoder='google_maps')), ('zoom', wagtailgeowidget.blocks.GeoZoomBlock(required=False)), ('map', wagtailgeowidget.blocks.GoogleMapsBlock(address_field='address', zoom_field='zoom'))]))]))])), ('hero_block', wagtail.core.blocks.StructBlock([('super_header', wagtail.core.blocks.CharBlock(required=False)), ('button_link', wagtail.core.blocks.StructBlock([('button_style', page.blocks.custom_choice_block.CustomChoiceBlock(choices=((' btn-link ', 'Link Style'), (' btn-primary ', 'Button Style')), default=' btn-primary ', label='Button Style', required=False, widget=django.forms.widgets.Select)), ('link_type', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('', 'None'), ('url', 'URL'), ('page', 'Page'), ('document', 'Document'), ('email', 'Email'), ('anchor', 'Anchor'), ('phone', 'Phone')), default='', label='Type', required=False, widget=django.forms.widgets.RadioSelect)), ('link_opens_in_new_tab', wagtail.core.blocks.BooleanBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(label='URL', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('email', wagtail.core.blocks.EmailBlock(required=False)), ('phone', wagtail.core.blocks.CharBlock(required=False)), ('anchor', wagtail.core.blocks.CharBlock(help_text='This will only work properly if there is an anchor block dropped on the home page', required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Text', required=False))])), ('hero_slides', wagtail.core.blocks.StreamBlock([('hero_slide', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock(required=False)), ('subheader', wagtail.core.blocks.RichTextBlock()), ('desktop_image', wagtail.images.blocks.ImageChooserBlock()), ('mobile_image', wagtail.images.blocks.ImageChooserBlock(required=False))]))]))])), ('quote_block', wagtail.core.blocks.StructBlock([('block_id', wagtail.core.blocks.CharBlock(required=False)), ('quote_text', wagtail.core.blocks.CharBlock()), ('quote_author_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('quote_author_name', wagtail.core.blocks.CharBlock()), ('quote_author_title', wagtail.core.blocks.CharBlock(required=False)), ('quote_author_title_2', wagtail.core.blocks.CharBlock(required=False))])), ('internal_hero_block', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock(required=False)), ('subheader', wagtail.core.blocks.RichTextBlock()), ('desktop_image', wagtail.images.blocks.ImageChooserBlock()), ('mobile_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('internal_hero_style', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('left-hero', 'Left Style Hero'), ('center-hero', 'Center Style Hero')), default='left-hero', label='Internal Hero Style', required=False, widget=django.forms.widgets.Select))]))], blank=True, null=True),
        ),
    ]
