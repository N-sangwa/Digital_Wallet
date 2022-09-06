# from ast import mod
# from distutils.command.upload import upload
# import email
# from inspect import signature
# from locale import currency
from tkinter import CASCADE
# from unicodedata import name
from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model) :
    first_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NBY', 'Non-Binary'),)

    gender = models.CharField(choices= GENDER_CHOICES, max_length=18, blank=True)
    address = models.TextField(blank=False)
    age = models.PositiveBigIntegerField(blank=False)
    nationality = models.CharField(max_length=15,blank=True)
    id_number = models.CharField(max_length=15, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models. EmailField(blank=False)
    profile_picture = models.ImageField ( upload_to = 'profile_picture', null = True)

    MARITAL_STATUS_CHOICES = (
        ('MARRIED', 'Married'),
        ('SINGLE', 'Single'),
                    )

    martal_status = models.CharField( max_length= 10,choices= MARITAL_STATUS_CHOICES, null=True)
    
    signature = models.ImageField (upload_to = 'signature image', blank = True)

    EMPLOYMENT_STATUS_CHOICES = ((True, 'True'),  (False, 'False'),)

    employment_status = models.BooleanField(choices= EMPLOYMENT_STATUS_CHOICES, blank= False)


    def __str__(self) -> str:
        return self.first_name +" " + self.last_name

        # return admin.register(Customer)


class Currency(models.Model) :
    name = models.CharField(max_length= 30)
    country = models.CharField(max_length=30)

    CURRENCY_CHOICES =(
        ('KENYAN SHILLINGS','Ksh'),
        ('RWANDAN FRANCS','Rwf'),
        ('UGANDAN SHILLINGS','Ugs'),
        ('DOLLARS','$'),
        ('TANZANIAN SHILLINGS','Tzs'),
        )
     
    symbol = models.CharField(choices=CURRENCY_CHOICES , max_length=100, blank=False)

    def __str__(self) -> str:
        return self.symbol


class Wallet(models.Model): 
    balance = models.IntegerField()
    customer= models.OneToOneField(Customer, on_delete=models.CASCADE)
    pin = models.SmallIntegerField()
    
    #inquire more on currency relationship
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    date_created = models.DateTimeField(default= timezone.now)

    CHOICES_TYPE = (
        ('Closed','Closed'),
        ('Semi-closed', 'Semi-closed'),
        ('Open', 'Open'),
    )

    type = models.CharField( choices=CHOICES_TYPE, max_length=50)
    
    CHOICES_WALLET_STATUS = (

        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    status = models.CharField(choices= CHOICES_WALLET_STATUS, max_length= 10, blank= True)

    def __str__(self) -> str: 
        return self.customer.first_name 


class Account (models.Model) :
    account_name = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50)
    balance = models.IntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.account_name

class Third_party (models.Model) :
    name = models.CharField(max_length= 50, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    email = models.EmailField(blank= False)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self) -> str :
        return self.name



class Transaction(models.Model) :
    TRANSACTION_TYPE_CHOICES = (
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAWAL', 'Withdraw'),
        ('TRANSFER', 'Transfer'),
    )

    transaction_type = models.CharField(choices=TRANSACTION_TYPE_CHOICES, max_length= 20)
    account_origin = models.ForeignKey(Account, related_name='account_destination',on_delete=models.CASCADE)
    account_destination = models.ForeignKey(Account, related_name= 'account_origin', on_delete=models.CASCADE)
    third_party = models.ForeignKey(Third_party, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default = timezone.now) 
    reciept = models.CharField(max_length=500, blank=False)
    
    TRANSACTION_STATUS = (
        ('PENDING', 'Pending'),
        ('SUCCESSFUL', 'Successful'),
    )

    status = models.CharField(choices=TRANSACTION_STATUS, max_length=10)

    def __str__(self) -> str :
        return self.reciept



class Card (models.Model) :
    card_number = models.IntegerField()
    date_issued = models.DateTimeField (default=timezone.now)
    expiry_date = models.DateTimeField(blank=False)
    security_code = models.SmallIntegerField()
    signature = models.ImageField(upload_to = 'profile_picture', null = True)
    issuer = models.CharField(max_length=50)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.account



class Notification (models.Model) : 
    message = models.CharField(max_length=500)
    recipient = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField(default=timezone.now)

    NOTIFICATION_STATUS_CHOICES = (
        ('READ', 'Read'),
        ('UNREAD', 'Unread'),
    )
    notification_status = models.CharField(choices=NOTIFICATION_STATUS_CHOICES, max_length=20, blank=True)

    def __str__(self) -> str:
        return self.message



class Receipt (models.Model):
    reciept_content = models.CharField(max_length=500, default=None)
    date = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField()
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    receipt_file = models.FileField(upload_to= 'uploads')

    def __str__(self) -> str :
        return self.reciept_content



class Reward(models.Model) :
    points = models.PositiveBigIntegerField()
    wallet = models.ForeignKey(Wallet, on_delete= models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)
    reward_note = models.CharField(max_length=500, default= None)

    def __str__(self) -> str:
        return self.reward_note






    

    

    
