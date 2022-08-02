from django.contrib import admin
from .models import Account, Card, Currency, Customer, Notification, Receipt, Reward, Third_party, Transaction, Wallet

# class CustomerAdmin(admin.ModelAdmin):
#     list_display= ('first_name', 'last_name', 'email',)
#     search_fields = ('first_name', 'last_name')

admin.site.register(Customer)
admin.site.register(Wallet)
admin.site.register(Currency)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Third_party)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Reward)




# Register your models here.

