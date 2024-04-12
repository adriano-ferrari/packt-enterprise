# Generated by Django 4.0 on 2024-04-12 22:58

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions
import django.db.models.functions.text
import django.utils.timezone
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Business Name')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=75, null=True, verbose_name='Engine')),
            ],
        ),
        migrations.CreateModel(
            name='engine3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=75, null=True, verbose_name='Engine')),
                ('other_name', models.CharField(blank=True, max_length=75, null=True, verbose_name='Other Engine Name')),
            ],
            options={
                'verbose_name': 'Practice Engine',
                'verbose_name_plural': 'Practice Engines',
                'db_table': 'chapter_3_practice_engine',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(blank=True, max_length=17, null=True, unique=True, verbose_name='VIN')),
                ('sold', models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, null=True, verbose_name='Sold?')),
                ('price_currency', djmoney.models.fields.CurrencyField(choices=[('EUR', 'EUR €'), ('USD', 'USD $')], default='USD', editable=False, max_length=3, null=True)),
                ('price', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator({'EUR': 500, 'USD': 400}), djmoney.models.validators.MaxMoneyValidator({'EUR': 500000, 'USD': 400000})])),
                ('make', models.PositiveIntegerField(blank=True, choices=[(0, '------'), (1, 'Buick'), (2, 'Cadillac'), (3, 'Chevrolet'), (4, 'Ford'), (5, 'GMC'), (6, 'Chrysler'), (7, 'Dodge'), (8, 'Jeep'), (9, 'Lincoln'), (10, 'Tesla')], null=True, verbose_name='Vehicle Make/Brand')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=75, null=True, unique=True, verbose_name='Model')),
                ('make', models.PositiveIntegerField(blank=True, choices=[(0, '------'), (1, 'Buick'), (2, 'Cadillac'), (3, 'Chevrolet'), (4, 'Ford'), (5, 'GMC'), (6, 'Chrysler'), (7, 'Dodge'), (8, 'Jeep'), (9, 'Lincoln'), (10, 'Tesla')], null=True, verbose_name='Make/Manufacturer')),
            ],
            options={
                'verbose_name': 'Vehicle Model',
                'verbose_name_plural': 'Vehicle Models',
                'ordering': ['name'],
            },
        ),
        migrations.AddIndex(
            model_name='vehiclemodel',
            index=models.Index(fields=['name'], name='chapter_3_v_name_7ccb3d_idx'),
        ),
        migrations.AddIndex(
            model_name='vehiclemodel',
            index=models.Index(fields=['-name'], name='desc_name_idx'),
        ),
        migrations.AddIndex(
            model_name='vehiclemodel',
            index=models.Index(django.db.models.expressions.OrderBy(django.db.models.functions.text.Lower('name'), descending=True), name='lower_name_idx'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='engine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='engine_vehicle', to='chapter_3.engine', verbose_name='Engine'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model_vehicle', to='chapter_3.vehiclemodel', verbose_name='Model'),
        ),
        migrations.AddField(
            model_name='engine3',
            name='vehicle_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model_engine2', to='chapter_3.vehiclemodel', verbose_name='Model'),
        ),
        migrations.AddField(
            model_name='engine',
            name='vehicle_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model_engine', to='chapter_3.vehiclemodel', verbose_name='Model'),
        ),
        migrations.AddField(
            model_name='seller',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='seller',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='seller',
            name='vehicles',
            field=models.ManyToManyField(blank=True, related_name='vehicle_sellers', related_query_name='vehicle_seller', to='chapter_3.Vehicle', verbose_name='Vehicles'),
        ),
    ]
