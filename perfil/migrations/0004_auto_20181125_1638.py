# Generated by Django 2.1.3 on 2018-11-25 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfil', '0003_perfil_contatos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='email',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='mensagem',
        ),
        migrations.AddField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
