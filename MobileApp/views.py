from django.shortcuts import render,redirect
from django.http import HttpResponse
from MobileApp.models import UserData,Mobiles

# Create your views here.
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        UserData.objects.create(username=username,email=email,password=password)
        return redirect('loginpage')
    else:
        return render(request,"./MobileApp/signup.html")
    
def login(request):
    if request.method == 'POST':
        user=UserData.objects.filter(
            username=request.POST.get("username"),
            password=request.POST.get("password")
        ).first()
        if user:
           return redirect("home")
        else:
            return redirect("loginpage")
    else:
        return render(request,"./MObileApp/login.html")

def home(request):
    search = request.POST.get("search")

    if search:
        mobiles = Mobiles.objects.filter(mobile_name__icontains=search)
    else:
        mobiles = Mobiles.objects.all()
    slider_mobiles = Mobiles.objects.order_by('-id')[:4]

    context = {
        "mobiles": mobiles,
        "slider_mobiles": slider_mobiles,
        "search": search
    }

    return render(request, "./MobileApp/home.html", context)