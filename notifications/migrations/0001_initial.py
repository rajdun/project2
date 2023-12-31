# Generated by Django 4.2.7 on 2023-11-20 00:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('color', models.CharField(choices=[('is-primary', 'Primary'), ('is-link', 'Link'), ('is-info', 'Info'), ('is-success', 'Success'), ('is-warning', 'Warning'), ('is-danger', 'Danger')], default='is-primary', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifications.notificationtemplate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
