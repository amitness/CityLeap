# Generated by Django 2.0.1 on 2018-01-04 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('upvote_count', models.IntegerField(default=True, null=True)),
                ('category', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
            ],
        ),
    ]
