# Generated by Django 4.0.6 on 2022-09-01 07:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=50)),
                ('account_type', models.CharField(max_length=50)),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('symbol', models.CharField(choices=[('KENYAN SHILLINGS', 'Ksh'), ('RWANDAN FRANCS', 'Rwf'), ('UGANDAN SHILLINGS', 'Ugs'), ('DOLLARS', '$'), ('TANZANIAN SHILLINGS', 'Tzs')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=15)),
                ('last_name', models.CharField(blank=True, max_length=15)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('NBY', 'Non-Binary')], max_length=18)),
                ('address', models.TextField()),
                ('age', models.PositiveBigIntegerField()),
                ('nationality', models.CharField(blank=True, max_length=15)),
                ('id_number', models.CharField(blank=True, max_length=15)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('profile_picture', models.ImageField(null=True, upload_to='profile_picture')),
                ('martal_status', models.CharField(choices=[('MARRIED', 'Married'), ('SINGLE', 'Single')], max_length=10, null=True)),
                ('signature', models.ImageField(blank=True, upload_to='signature image')),
                ('employment_status', models.BooleanField(choices=[(True, 'True'), (False, 'False')])),
            ],
        ),
        migrations.CreateModel(
            name='Third_party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('pin', models.SmallIntegerField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('Closed', 'Closed'), ('Semi-closed', 'Semi-closed'), ('Open', 'Open')], max_length=50)),
                ('status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=10)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.currency')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('DEPOSIT', 'Deposit'), ('WITHDRAWAL', 'Withdraw'), ('TRANSFER', 'Transfer')], max_length=20)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('reciept', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('SUCCESSFUL', 'Successful')], max_length=10)),
                ('account_destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_origin', to='wallet.account')),
                ('account_origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_destination', to='wallet.account')),
                ('third_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.third_party')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveBigIntegerField()),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('reward_note', models.CharField(default=None, max_length=500)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciept_content', models.CharField(default=None, max_length=500)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.IntegerField()),
                ('receipt_file', models.FileField(upload_to='uploads')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('date_and_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('notification_status', models.CharField(blank=True, choices=[('READ', 'Read'), ('UNREAD', 'Unread')], max_length=20)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField()),
                ('date_issued', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField()),
                ('security_code', models.SmallIntegerField()),
                ('signature', models.ImageField(null=True, upload_to='profile_picture')),
                ('issuer', models.CharField(max_length=50)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet'),
        ),
    ]
