# Generated by Django 4.1.2 on 2022-11-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_post_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="like_count",
            field=models.IntegerField(blank=True, default=0, verbose_name="heart"),
        ),
    ]
