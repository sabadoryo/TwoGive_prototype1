# Generated by Django 2.2.6 on 2019-10-28 07:59

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0011_update_proxy_permissions'),
        ('TwoGive', '0002_auto_20191025_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='authUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('iin', models.CharField(max_length=12)),
                ('is_renter', models.BooleanField(default=False)),
                ('num_tel', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]