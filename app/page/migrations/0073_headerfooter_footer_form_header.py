# Generated by Django 3.2.19 on 2023-07-31 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0072_alter_headerfooter_footer_contact_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerfooter',
            name='footer_form_header',
            field=models.CharField(blank=True, default='', max_length=512, null=True),
        ),
    ]
