from django.http import HttpResponse # to use HttpResponse
from django.shortcuts import render, redirect
from .models import Member, Earning, Expense # models we made
from .forms import MemberForm, EarningForm, ExpenseForm

# Create your views here.

def familytracker(request):

    # Pulls all rows from the Member, Earning, and Expense tables.
    # (Fetching Data [It fetches all rows (i.e., all records/entries) from the table])
    members = Member.objects.all()
    earnings = Earning.objects.all()
    expenses = Expense.objects.all()

    total_earnings = sum(e.amount for e in earnings) # total_earnings: Adds up all earning amounts.
    total_expenses = sum(e.amount for e in expenses) # total_expenses: Adds up all expense amounts.
    balance = total_earnings - total_expenses # balance: Net balance = earnings - expenses.

    if request.method == 'POST': # If it’s a POST request (form was submitted)
        
        # Each form has a unique name (add_member, add_earning, add_expense) to differentiate them.
        if 'add_member' in request.POST: # it checks which form button was clicked.
            member_form = MemberForm(request.POST) # Creates the form (named member_form) from the request.
            if member_form.is_valid(): # check it's valid or not
                member_form.save() # Saves it to the DataBase
                return redirect('familytracker') # Redirects back to the dashboard (i.e., reloads the page).
            
        elif 'add_earning' in request.POST: # it checks which form button was clicked.
            earning_form = EarningForm(request.POST) # Creates the form (named earning_form) from the request.
            if earning_form.is_valid(): # check it's valid or not
                earning_form.save() # Saves it to the DataBase
                return redirect('familytracker') # Redirects back to the dashboard (i.e., reloads the page).
            
        elif 'add_expense' in request.POST: # it checks which form button was clicked.
            expense_form = ExpenseForm(request.POST) # Creates the form (named expense_form) from the request.
            if expense_form.is_valid(): # check it's valid or not
                expense_form.save() # Saves it to the DataBase
                return redirect('familytracker') # Redirects back to the dashboard (i.e., reloads the page).
    
    # On GET Request: Show Blank Forms
    # If not a POST request, then user is just visiting the page
    # Blank forms are initialized to be rendered in the template.
    else:
        member_form = MemberForm()
        earning_form = EarningForm()
        expense_form = ExpenseForm()
    
    return render (request, "familytracker/family.html", {
        'members': members,
        'earnings': earnings,
        'expenses': expenses,
        'balance': balance,
        'total_earnings': total_earnings,
        'total_expenses': total_expenses,
        'member_form': member_form,
        'earning_form': earning_form,
        'expense_form': expense_form,
    })
