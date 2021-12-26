# Generated by Django 4.0 on 2021-12-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignedUp',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('dob', models.DateField()),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='sno',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='sno',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]