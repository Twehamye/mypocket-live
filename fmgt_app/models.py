from django.db import models
import datetime
from datetime import date  
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator


class Income(models.Model):
	nature_choices =(("daily","daily"),("weekly","weekly"),
                        ("monthly","monthly"),("other","other"))

	date_of_income = models.DateField()
	source = models.CharField(max_length=300, null=False)
	amount = models.PositiveIntegerField()
	nature = models.CharField(max_length=100, null=False, choices = nature_choices)
	referal =models.CharField(max_length=100, null=False)
        

class Expense(models.Model):
	nature_choices =(("daily","daily"),("weekly","weekly"),
                        ("monthly","monthly"),("other","other"))

	date_of_expense = models.DateField()
	purpose = models.CharField(max_length=300, null=False)
	nature = models.CharField(max_length=300, null=False, choices = nature_choices)
	amount = models.PositiveIntegerField()       


class Loan(models.Model):
    status_choices =(("advanced","advanced"),("received","received"))

    month_choices = (("January","January"),("February","February"),("March","March"),
    				("April","April"),("May","May"),("June","June"),("July","July"),
    				("August","August"),("September","September"),("October","October"),
    				("November","November"),("December","December"))

    loan_id =models.CharField(max_length=10, primary_key=True )
    responsible = models.CharField(max_length=300, null=False)
    amount = models.PositiveIntegerField()
    interest =models.PositiveIntegerField()
    no_installments =models.PositiveIntegerField()
    month = models.CharField(max_length=200, null=False, choices = month_choices)      
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, null=False, choices = status_choices)
    payment_date =models.DateField()
    
    def __str__(self):

        return self.loan_id + " " + self.responsible

    @property
    def total_amount(self):
        return (self.amount + self.interest)


class LoanPayment(models.Model):
	loan_status_choices =(("unpaid","unpaid"),("partly_paid","partly_paid"),("fully_paid","fully_paid"))

	loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
	amount_paid = models.PositiveIntegerField()
	payment_date = models.DateField()
	loan_status =models.CharField(max_length=200, null=False, choices = loan_status_choices)


class Asset(models.Model):
	date_of_acquisition = models.DateField()
	asset_name = models.CharField(max_length=300, null=False)
	asset_cost = models.PositiveIntegerField()
	description = models.CharField(max_length=500, null=False)
	refere1 =models.CharField(max_length=100, null=False)
	refere1_phone = models.PositiveIntegerField()
	refere2 =models.CharField(max_length=100, null=False)
	refere2_phone = models.PositiveIntegerField()



	# class Leave(models.Model):
    # from_date = models.DateField()
    # to_date = models.DateField()

    # def __str__(self):
    #     return self.name

    # @property
    # def date_diff(self):
    #     return (self.to_date - self.from_date).days

	# 	and in your template you could use it as {{ leave_object.date_diff }}