# Generated by Django 2.2.6 on 2019-11-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TwoGive', '0008_cart_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(null=True, on_delete='CASCADE', to='TwoGive.Cart')),
                ('product', models.ForeignKey(null=True, on_delete='CASCADE', to='TwoGive.Item')),
            ],
        ),
    ]
