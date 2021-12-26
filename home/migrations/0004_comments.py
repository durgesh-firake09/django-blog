# Generated by Django 4.0 on 2021-12-26 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_signedup_alter_contact_sno_alter_post_sno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment_body', models.TextField()),
                ('posted_on', models.DateField()),
                ('postSno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.post')),
                ('user_posted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.signedup')),
            ],
        ),
    ]