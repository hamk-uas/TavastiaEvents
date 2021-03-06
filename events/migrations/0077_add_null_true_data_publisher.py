# Generated by Django 2.2.9 on 2020-05-19 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0076_change_image_licence_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='data_source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provided_event_data', to=settings.DJANGO_ORGHIERARCHY_DATASOURCE_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='published_events', to='django_orghierarchy.Organization', verbose_name='Publisher'),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='data_source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provided_keyword_data', to=settings.DJANGO_ORGHIERARCHY_DATASOURCE_MODEL),
        ),
        migrations.AlterField(
            model_name='keywordset',
            name='data_source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provided_keywordset_data', to=settings.DJANGO_ORGHIERARCHY_DATASOURCE_MODEL),
        ),
        migrations.AlterField(
            model_name='place',
            name='data_source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provided_place_data', to=settings.DJANGO_ORGHIERARCHY_DATASOURCE_MODEL),
        ),
        migrations.AlterField(
            model_name='place',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_orghierarchy.Organization', verbose_name='Publisher'),
        ),
    ]
