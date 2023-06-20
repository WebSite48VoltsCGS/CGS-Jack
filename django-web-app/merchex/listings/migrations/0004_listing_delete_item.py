# Generated by Django 4.2.2 on 2023-06-16 07:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('sold', models.BooleanField(default=False)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2023)])),
                ('type', models.CharField(choices=[('RCD', 'Records'), ('CTH', 'Clohting'), ('POST', 'Posters'), ('MISC', 'Miscellaneous')], max_length=20)),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]