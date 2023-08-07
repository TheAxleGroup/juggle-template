# Generated by Django 3.2.19 on 2023-07-17 20:41

from django.db import migrations
import django.forms.widgets
import page.blocks.custom_choice_block
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0054_alter_social_socials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='socials',
            field=wagtail.core.fields.StreamField([('social_item', wagtail.core.blocks.StructBlock([('icon_class', page.blocks.custom_choice_block.CustomChoiceBlock(choices=(('fab fa-facebook', 'Facebook'), ('fab fa-twitter', 'Twitter'), ('fab fa-linkedin-in', 'LinkedIn'), ('fab fa-instagram', 'Instagram'), ('fab fa-tiktok', 'TikTok'), ('fab fa-youtube', 'YouTube'), ('fab fa-spotify', 'Spotify')), default='fab fa-facebook', label='Social', widget=django.forms.widgets.RadioSelect)), ('link', wagtail.core.blocks.URLBlock())]))], blank=True, null=True),
        ),
    ]
