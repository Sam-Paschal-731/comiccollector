# Generated by Django 4.0.3 on 2022-04-12 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[('0', 'Zero'), ('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_text',
            field=models.TextField(max_length=100),
        ),
    ]
