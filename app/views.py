from django.shortcuts import redirect, render

from app.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def index(request):
    data=Student.objects.all()
    return render(request,"app/index.html",{'data':data})
def insertdata(request):
    if request.method =="POST":# Here condition is -> if user clicks on the submit button 
        name1=request.POST.get('name') # Here we are storing name from (index.html) file in name1 variable
        email1=request.POST.get("email")
        age1=request.POST.get("age")
        gender1=request.POST.get("gender")
        query=Student(name=name1,email=email1,age=age1,gender=gender1)# Here we are assigning value of name1 to name variable
        query.save()
        return redirect("/")
    return render(request,"app/index.html")
def updateData(request,id):
    d=Student.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get('name') # we are bringing the name(text box) from index.html file to name (variable)
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        x=Student.objects.get(id=id)
        x.name=name
        x.email=email
        x.age=age
        x.gender=gender
        x.save()
        return redirect('/')
    return render(request,"app/edit.html",{'d':d})
def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    return redirect('/')
def register(request):
    if request.method=="POST": # if user clicks on register button
        form=UserCreationForm(request.POST)
        if form.is_valid(): # if the form is valid (if user was registerd with correct userid and password )
            form.save() # then save that details
            return redirect('login') # after registering succesffully page will redirects to login page
    else:
        form=UserCreationForm()
    return render(request,"app/register.html",{'form':form})

