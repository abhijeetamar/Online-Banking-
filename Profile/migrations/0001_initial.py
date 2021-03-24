# Generated by Django 3.1.6 on 2021-03-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=1)),
                ('annual_income', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('mobile', models.IntegerField(max_length=15)),
                ('occupation', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('user_name', models.CharField(max_length=150)),
                ('aadhar', models.IntegerField(max_length=12)),
                ('image', models.ImageField(upload_to='uploads/Photo')),
            ],
        ),
        migrations.CreateModel(
            name='PresentLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='India', max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('user_name', models.CharField(default=None, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('user_name', models.CharField(max_length=150)),
            ],
        ),
    ]