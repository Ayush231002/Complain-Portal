from django.shortcuts import render,redirect
from.models import sign

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        dob=request.POST['dob']
        address=request.POST['address']
        sign(name=name,email=email,contact=contact,dob=dob,address=address).save()
        msg='Sign-UP Done'
        return render(request,'signup.html',{'msg':msg})    
    return render(request,'signup.html')
    
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        dob=request.POST['dob']
        contact=request.POST['contact']
        if sign.objects.filter(email=email,dob=dob,contact=contact):
            return redirect('profile')
        else:
            msg="Invalid Credentials"
            return render(request, 'login.html',{'msg':msg})    
    return render(request, 'login.html')
def profile(request):
    return render(request, 'profile.html')




def delete(request):
    if request.method=="POST":
        email=request.POST['email']
        if sign.objects.filter(email=email):
            sign.objects.filter(email=email).delete()
            msg='Data Deleted'
            return render(request, 'delete.html',{'msg':msg})
        else:
            msg="Data Not Found"
            return render(request, 'delete.html',{'msg':msg})
    else:
        return render(request, 'delete.html')
    
def edit(request):
    if request.method=="POST":
        email=request.POST['email']
        name=request.POST['name']
        if sign.objects.filter(email=email):
            sign.objects.filter(email=email).update(name=name)
            msg='Update Successfully'
            return render(request, 'update.html',{'msg':msg})
        else:
            msg="Invalid Email"
            return render(request, 'update.html',{'msg':msg})
    else:
        return render(request, 'update.html')    

