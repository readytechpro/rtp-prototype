# Generated by Django 3.1.2 on 2021-03-12 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerProjectDetailCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('heading', models.CharField(max_length=150)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteering.volunteerproject')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerProjectDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('detail_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteering.volunteerprojectdetailcategory')),
            ],
        ),
    ]
