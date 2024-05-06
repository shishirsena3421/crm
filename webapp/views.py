from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record

from django.contrib import messages


def home(request):

    return render(request, 'webapp/index.html')


def register(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()


            messages.success(request, "Account created successfully!!!!")

            return redirect("my-login")

    context = {'form':form}
    return render(request, 'webapp/register.html', context=context)



# login a user

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                messages.success(request, "You have logged in")

                return redirect("dashboard")

                

    context = {'form':form} 

    return render(request, 'webapp/my-login.html', context=context)           





# DASHBOARD


@login_required(login_url='my-login')

def dashboard(request):
    my_records = Record.objects.filter(user=request.user)
    #my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'webapp/dashboard.html', context=context)





# logout a user



def user_logout(request):

    auth.logout(request)

    return redirect("my-login")


# - Create a Record

@login_required(login_url='my-login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)  # Save the form temporarily without committing to the DB
            record.user = request.user        # Set the current user as the owner of the record
            record.save()                     # Now save the record into the database
            messages.success(request, "Record is created successfully!!!!")
            return redirect("dashboard")
    context = {'form': form}
    return render(request, 'webapp/create-record.html', context=context)

# update a record


@login_required(login_url='my-login')

def update_record(request,pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Record updated successfully!!!!")

            return redirect("dashboard")

    context = {'form' : form}

    return render(request, 'webapp/update-record.html', context = context)


# Read or View a Single record


@login_required(login_url='my-login')

def singular_record(request,pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'webapp/view-record.html', context = context )



# Delete a record


@login_required(login_url='my-login')
def delete_record(request,pk):

    record = Record.objects.get(id=pk)
    record.delete()


    messages.success(request, "Record deleted")
    return redirect("dashboard")



def payment(request):

    return render(request, 'webapp/payment.html')