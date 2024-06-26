# Generated by Django 4.2.13 on 2024-06-03 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0002_alter_hotel_hid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending'), ('processing', 'Processing'), ('cancelled', 'Cancelled'), ('initiated', 'Initiated'), ('failed', 'Failed'), ('refunding', 'Refunding'), ('refunded', 'Refunded'), ('expired', 'Expired')], max_length=100)),
                ('fullname', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=1000)),
                ('phone', models.CharField(max_length=20)),
                ('before_discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('saved', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('total_days', models.PositiveIntegerField(default=0)),
                ('num_adult', models.PositiveIntegerField(default=1)),
                ('num_chieldren', models.PositiveIntegerField(default=0)),
                ('check_in', models.BooleanField(default=False)),
                ('check_out', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('striped_payment_intent', models.CharField(blank=True, max_length=1000, null=True)),
                ('success_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('booking_id', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz123', length=22, max_length=22, prefix='', unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Disable', 'Disable'), ('Rejected', 'Rejected'), ('In Review', 'In Review'), ('Live', 'Live')], max_length=20),
        ),
        migrations.CreateModel(
            name='StaffOnDuty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.booking')),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('number_of_beds', models.PositiveIntegerField(default=0)),
                ('rtid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz123', length=22, max_length=22, prefix='', unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
            options={
                'verbose_name_plural': 'Room Type',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10000)),
                ('is_avaliable', models.BooleanField(default=True)),
                ('rid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz123', length=22, max_length=22, prefix='', unique=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.roomtype')),
            ],
            options={
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='HotelGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='hotel_gallery')),
                ('hid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz123', length=22, max_length=22, prefix='', unique=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
            options={
                'verbose_name_plural': 'Hotel Gallery',
            },
        ),
        migrations.CreateModel(
            name='HotelFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_type', models.CharField(blank=True, choices=[('Bootstrap Icons', 'Draft'), ('Fontawesome Icons', 'Disable'), ('Box Icons', 'Rejected'), ('Remi Icons', 'Remi Icons'), ('Flat Icons', 'Flat Icons')], max_length=100, null=True)),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
            options={
                'verbose_name_plural': 'Hotel Feature',
            },
        ),
        migrations.CreateModel(
            name='HotelFaqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
            options={
                'verbose_name_plural': 'Hotel Gallery',
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel'),
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ManyToManyField(to='hotel.room'),
        ),
        migrations.AddField(
            model_name='booking',
            name='room_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.roomtype'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess_out', models.DateTimeField(auto_now_add=True)),
                ('guess_in', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.booking')),
            ],
        ),
    ]
