# Generated by Django 3.1.3 on 2020-11-24 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaceLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FaceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_image', models.ImageField(max_length=200, upload_to='')),
                ('face_image', models.ImageField(editable=False, max_length=250, upload_to='')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='face_images', to='faces.facelabel')),
            ],
        ),
    ]