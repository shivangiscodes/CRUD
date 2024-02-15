from django.shortcuts import render, redirect
from .models import Employees

# Create your views here.
def INDEX(request):
    emp = Employees.objects.all()
    context = {
        'emp':emp,
    }
    return render(request,'index.html',context)


#no id
#if we use id here, then it gets updated
#if we dont use id here then it creates a new record
def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        # Assuming 'name', 'email', 'address', and 'phone' are the names given to your form fields

        # Create a new instance of Employees model and save it
        employee = Employees.objects.create(name=name, email=email, address=address, phone_number=phone)
        employee.save()
        return redirect('home')  # Redirect to a page where all employees are listed
    return render(request, 'index.html')

#id
def Edit(request):
    emp = Employees.objects.all()

    context = {'emp':emp,}

    return redirect(request,'index.html',context)

#add and update are same
def Update(request,id):
    if request.method=='POST':
        name = request.POST.get('name')
        email= request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            id = id,
            name = name,
            email = email,
            address = address,
            phone_number = phone, 
        )

        emp.save()
        return redirect('home')

    return redirect(request,'index.html')

def Delete(request,id):
    emp = Employees.objects.filter(id = id).delete() #if we remove id, then all the data will get deleted
    #context = {'emp':emp,}
    return redirect('home')
    #return redirect(request,'index.html',context)