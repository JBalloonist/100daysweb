# Generated by Django 2.2.1 on 2019-05-28 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('source', models.URLField(blank=True, null=True)),
                ('cover', models.URLField(blank=True, null=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
    ]
