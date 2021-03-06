# Generated by Django 3.2.6 on 2021-08-29 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_tokens', models.IntegerField()),
                ('price_per_token', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('progress', models.IntegerField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='Users.customer')),
            ],
        ),
        migrations.CreateModel(
            name='UnsuccessfulBid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='unsuccessful', to='Bid.bid')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='unsuccessful_bid', to='Users.customer')),
            ],
        ),
        migrations.CreateModel(
            name='SuccessfulBid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_tokens_allotted', models.IntegerField()),
                ('bid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='successful', to='Bid.bid')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='successful_bid', to='Users.customer')),
            ],
        ),
    ]
