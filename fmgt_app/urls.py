from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("", views.home, name='home'),

	path('create_expense/', views.createExpense, name='create_expense'),
    path('update_expense/<int:id>/', views.updateExpense, name='update_expense'),
    path('delete_expense/<int:id>/', views.deleteExpense, name='delete_expense'),

    path('create_income/', views.createIncome, name='create_income'),
    path('update_income/<int:id>/', views.updateIncome, name='update_income'),
    path('delete_income/<int:id>/', views.deleteIncome, name='delete_income'),

    path('create_loan/', views.createLoan, name='create_loan'),
    path('update_loan/<int:id>/', views.updateLoan, name='update_loan'),
    path('delete_loan/<int:id>/', views.deleteLoan, name='delete_loan'),

    path('create_asset/', views.createAsset, name='create_asset'),
    path('update_asset/<int:id>/', views.updateAsset, name='update_asset'),
    path('delete_asset/<int:id>/', views.deleteAsset, name='delete_asset'),

    path('all_expenses/', views.allExpense, name='all_expenses'),
    path('all_income/', views.allIncome, name='all_income'),
    path('all_loans/', views.allLoan, name='all_loans'),
    path('all_assets/', views.allAsset, name='all_assets'),


]