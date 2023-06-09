# Generated by Django 4.1.2 on 2022-11-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('desc', models.TextField(max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('clas', models.CharField(max_length=50, null=True)),
                ('roll', models.IntegerField(default=0, null=True)),
                ('desc', models.TextField(max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('date', models.DateTimeField()),
                ('content', models.FileField(default=None, null=True, upload_to='notice/')),
                ('desc', models.TextField(max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='stu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.CharField(max_length=50, null=True)),
                ('c', models.CharField(max_length=50, null=True)),
                ('r', models.CharField(max_length=50, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('father', models.CharField(max_length=50, null=True)),
                ('mother', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('guardian', models.CharField(max_length=50, null=True)),
                ('mobile', models.IntegerField(default=0, null=True)),
                ('imergency', models.IntegerField(default=0, null=True)),
                ('bloodgroup', models.CharField(max_length=50, null=True)),
                ('b', models.IntegerField(default=0, null=True)),
                ('e', models.IntegerField(default=0, null=True)),
                ('s', models.IntegerField(default=0, null=True)),
                ('m', models.IntegerField(default=0, null=True)),
                ('tm', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('_clas', models.CharField(max_length=50, null=True)),
                ('roll', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('password1', models.CharField(max_length=50, null=True)),
                ('password2', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
