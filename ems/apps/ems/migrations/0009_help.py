# Generated by Django 2.2.3 on 2019-08-29 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0008_element_configuration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=None, max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
