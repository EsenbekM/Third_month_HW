# Generated by Django 3.2.8 on 2021-10-26 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='media/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=50)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
