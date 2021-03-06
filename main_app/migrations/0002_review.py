# Generated by Django 4.0.3 on 2022-04-12 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='review date')),
                ('rating', models.IntegerField()),
                ('review_text', models.TextField(choices=[('0', 'Zero'), ('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], max_length=100)),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.comic')),
            ],
        ),
    ]
