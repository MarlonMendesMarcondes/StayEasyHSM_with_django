# Generated by Django 4.2.13 on 2024-06-09 23:33

from django.db import migrations
import django_ckeditor_5.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('hotel', '0003_booking_alter_hotel_description_alter_hotel_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='tags',
        ),
        migrations.AddField(
            model_name='hotel',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
