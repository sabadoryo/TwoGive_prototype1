# Generated by Django 2.2.6 on 2019-10-25 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('TwoGive', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_mybro',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.DeleteModel(
            name='Renter',
        ),
    ]