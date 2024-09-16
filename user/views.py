from django.shortcuts import render,redirect
from django.contrib.auth.models import User #User Model
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from user.models import Address
# Create your views here.
@never_cache
def signup(request):
    if request.user.is_authenticated:
        redirect("all_books")
    if request.method=='POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        # print(first_name,last_name,username,email,password)
        user_exists=False
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username is already Taken,Try with new one")
            user_exists=True
        if User.objects.filter(email=email).exists():
           messages.error(request,"E-mail is already Taken,Try with new one")
           user_exists=True
        if user_exists:
            return render(request,'user/signup.html')
        user=User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )
        user.save()
        messages.success(request,"Account Created Successfully Login To Continue")
    return render(request,'user/signup.html')

def signin(request):
    if request.user.is_authenticated:
        redirect("all_books")
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is None:
            messages.error(request,"Invalid Username or Password")
            return render(request,'user/signin.html')
        else:
            login(request,user)
            return redirect("all_books")
    return render(request,'user/signin.html')

def signout(request):
    logout(request)
    return render(request,'user/signin.html')

@login_required(login_url='/user/signin')
def profile(request):
    return render(request, 'user/profile.html')



def add_address(request):
    if request.method == 'POST':
        address_line_one = request.POST.get('address_line_one')
        address_line_two = request.POST.get('address_line_two')
        locality = request.POST.get('locality')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        zip = request.POST.get('zip')
        mobile = request.POST.get('mobile')
        
        address=Address(
            user=request.user,
            address_line_one=address_line_one,
            address_line_two=address_line_two,
            locality=locality,
            city=city,
            state=state,
            country=country,
            zip=zip,
            mobile=mobile
        )
        address.save()
    return redirect('check_out')

