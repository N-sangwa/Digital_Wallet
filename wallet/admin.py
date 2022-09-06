from django.contrib import admin
from .models import Account, Card, Currency, Customer, Notification, Receipt, Reward, Third_party, Transaction, Wallet


class CustomerAdmin(admin.ModelAdmin):
    list_display= ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
   

class WalletAdmin(admin.ModelAdmin):
    list_display = ('customer', 'balance', 'type')
    search_fields = ('customer','type')


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country','symbol')
    search_fields = ('name', 'symbol')


class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'account_type', 'balance')
    search_fields = ('account_name', 'account_type')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'account_origin', 'account_destination')
    search_fields = ('transaction_type', 'reciept')



class CardAdmin(admin.ModelAdmin):
    list_display = ('card_number','issuer', 'account')
    search_fields = ('card_number', 'account')

class Third_partyAdmin(admin.ModelAdmin):
    list_display = ('name', 'account', 'email')
    search_fields = ('name', 'email')


class NotificationAdmin(admin.ModelAdmin):
  list_display = ('recipient', 'date_and_time', 'notification_status')
  search_fields = ('recipient', 'date_and_time')


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('date', 'transaction', 'amount')
    search_fields = ('date', 'transaction')


class RewardAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'wallet', 'points')
    search_fields = ('date_time', 'wallet')



admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet,WalletAdmin)
admin.site.register(Currency,CurrencyAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Card,CardAdmin)
admin.site.register(Third_party,Third_partyAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(Receipt,ReceiptAdmin)
admin.site.register(Reward,RewardAdmin)
admin.site.register(Account,AccountAdmin)

# Register your models here.

