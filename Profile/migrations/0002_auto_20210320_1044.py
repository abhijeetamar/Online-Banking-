# Generated by Django 3.1.6 on 2021-03-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('To', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='basicdetails',
            name='aadhar',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='basicdetails',
            name='mobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='presentlocation',
            name='user_name',
            field=models.CharField(max_length=150),
        ),
    ]
