from django.contrib import admin
from .models import *

# admin.site.register(Expense)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
	list_display = ('date_of_expense', 'purpose','nature','amount' )



@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
	list_display = ('date_of_income', 'source','nature','amount','referal' )

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
	list_display = ('loan_id','date_created', 'responsible','amount','interest','no_installments','month','status','payment_date' )

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
	list_display = ('date_of_acquisition', 'asset_name','asset_cost','description','refere1','refere1_phone','refere2','refere2_phone' )