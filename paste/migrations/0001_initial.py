# Generated by Django 5.1.6 on 2025-02-18 11:53

import paste.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=paste.models.rand_title, max_length=128)),
                ('language', models.CharField(choices=[('Python', 'Python'), ('C++', 'Cpp'), ('C', 'C'), ('Javsacript', 'Js'), ('Java', 'Java'), ('C#', 'Csharp'), ('Other', 'Misc')], default='Other', max_length=10)),
                ('text', models.TextField()),
            ],
        ),
    ]
