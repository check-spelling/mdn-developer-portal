# Generated by Django 2.2.3 on 2019-07-25 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20190718_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='featured',
        ),
        migrations.AddField(
            model_name='events',
            name='featured_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='events.Event'),
        ),
    ]