from django.shortcuts import render
from .models import *
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExpenseForm, IncomeForm, LoanForm, AssetForm

def home(request):
    expense_list = Expense.objects.all()  
         

    context = {
                'expense_list': expense_list, 
                    
        }  

    return render(request, 'index.html', context )


def createExpense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm()
    return render(request, 'create_expense.html', {'form': form})


def updateExpense(request, id):
    expense = Expense.objects.get(id=id)
    form = ExpenseForm(instance=expense)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('all_expense')

    context = {'form': form } 

    return render(request, 'create_expense.html', context)  

def deleteExpense(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == "POST":
        expense.delete()
        return redirect('all_expense')

    context = {'expense': expense } 

    return render(request, 'delete_expense.html', context)   


def allExpense(request):
    expenses = Expense.objects.all().order_by("-date_of_expense")

    context = {'expenses': expenses }  

    return render(request, 'all_expenses.html', context )


def createIncome(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_income')
    else:
        form = IncomeForm()
    return render(request, 'create_income.html', {'form': form})


def updateIncome(request, id):
    income = Income.objects.get(id=id)
    form = IncomeForm(instance=income)

    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('all_income')

    context = {'form': form } 

    return render(request, 'create_income.html', context)         

def deleteIncome(request, id):
    income = Income.objects.get(id=id)
    if request.method == "POST":
        income.delete()
        return redirect('all_income')

    context = {'income': income } 

    return render(request, 'delete_income.html', context)   

def allIncome(request):

    income_list = Income.objects.all()  
         

    context = {
                'income_list': income_list, 
                    
        }  

    return render(request, 'all_income.html', context )


def createLoan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_loans')
    else:
        form = LoanForm()
    return render(request, 'create_loan.html', {'form': form})


def updateLoan(request, id):
    loan = Loan.objects.get(id=id)
    form = LoanForm(instance=loan)

    if request.method == "POST":
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            form.save()
            return redirect('all_loans')

    context = {'form': form } 

    return render(request, 'create_loan.html', context)         

def deleteLoan(request, id):
    loan = Loan.objects.get(id=id)
    if request.method == "POST":
        loan.delete()
        return redirect('all_loan')

    context = {'loan': loan } 

    return render(request, 'delete_loan.html', context) 

def allLoan(request):
    loans = Loan.objects.all().order_by("-date_created")
    
    context = {'loans': loans }  

    return render(request, 'all_loans.html', context )


def createAsset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_assets')
    else:
        form = AssetForm()
    return render(request, 'create_asset.html', {'form': form})


def updateAsset(request, id):
    asset = Asset.objects.get(id=id)
    form = AssetForm(instance=asset)

    if request.method == "POST":
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('all_assets')

    context = {'form': form } 

    return render(request, 'create_asset.html', context)         

def deleteAsset(request, id):
    asset = Asset.objects.get(id=id)
    if request.method == "POST":
        income.delete()
        return redirect('all_assets')

    context = {'asset': asset } 

    return render(request, 'delete_assets.html', context)   

def allAsset(request):

    asset_list = Asset.objects.all()  
         

    context = {
                'asset_list': asset_list, 
                    
        }  

    return render(request, 'all_assets.html', context )