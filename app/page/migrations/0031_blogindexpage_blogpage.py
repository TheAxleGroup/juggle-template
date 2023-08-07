# Generated by Django 3.2.12 on 2022-06-13 20:46

from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.routable_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('mediamodels', '0002_auto_20210809_0949'),
        ('page', '0030_alter_defaultpage_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('defaultpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='page.defaultpage')),
            ],
            options={
                'verbose_name': 'Blog Index Page',
                'verbose_name_plural': 'Blog Index Pages',
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'page.defaultpage'),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('defaultpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='page.defaultpage')),
                ('cover_image', models.ForeignKey(help_text='Logo used for featured block', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cover_image', to='mediamodels.customimage')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'page.defaultpage'),
        ),
    ]
