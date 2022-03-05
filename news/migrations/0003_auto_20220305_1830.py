# Generated by Django 3.1.14 on 2022-03-05 18:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_auto_20220305_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='points',
            field=models.ManyToManyField(blank=True, null=True, related_name='points', to=settings.AUTH_USER_MODEL),
        ),
    ]