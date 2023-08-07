# Generated by Django 3.2.16 on 2022-11-25 22:29

from django.db import migrations, models
import django.db.models.deletion
import wagtailcache.cache


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('mediamodels', '0002_auto_20210809_0949'),
        ('page', '0033_alter_defaultpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultpage',
            name='og_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='mediamodels.customimage', verbose_name='OG:Image'),
        ),
        migrations.CreateModel(
            name='CampaignPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('canonical_url', models.CharField(blank=True, help_text='Leave this blank unless you know there is a canonical URL for this content.', max_length=255, null=True, verbose_name='Canonical URL')),
                ('meta_keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Keywords')),
                ('exclude_from_sitemap', models.BooleanField(default=False, help_text='Removes this page from sitemap.xml')),
                ('og_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='OG:Title')),
                ('og_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='OG:Type')),
                ('og_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='OG:URL')),
                ('og_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='OG:Description')),
                ('og_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='mediamodels.customimage', verbose_name='OG:Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailcache.cache.WagtailCacheMixin, 'wagtailcore.page'),
        ),
    ]
