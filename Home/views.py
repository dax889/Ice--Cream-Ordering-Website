from django.shortcuts import render ,redirect,HttpResponse,get_object_or_404
from datetime import datetime
from Home.models import Contact,LoginRecord,SignupRecord,FeedbackForm,Product
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import IceCream
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound

# Create your views here.
def index(request):
    # context = {
    #     "variable1":"Dax is great",
    #     "variable2":"Harsh is great"
    flavour_data = {
    "name": "Vanilla",
    "description": "Classic and creamy Vanilla ice cream.",
    "items": [
            {
                "id": 0,
                "image": "5.jpg",
                "type": "Cup",
                "price": 50
            },
            {
                "id": 1,
                "image": "6.jpg",
                "type": "Cone",
                "price": 60
            },
            {
                "id": 2,
                "image": "7.jpg",
                "type": "Family Pack",
                "price": 150
            },
            {
                "id": 3,
                "image": "5.jpg",
                "type": "Cup",
                "price": 50
            },
            {
                "id": 4,
                "image": "6.jpg",
                "type": "Cone",
                "price": 60
            },
            {
                "id": 5,
                "image": "7.jpg",
                "type": "Family Pack",
                "price": 150
            },
        ]
    }

    return render(request, "index.html", {
        "flavour": flavour_data
    })

    # return render(request,'index.html')
    # return HttpResponse("this is home page")
    

def about(request):
    return render(request,'about.html')

    # return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html')

    # return HttpResponse("this is Services page")
def Ordernow(request):
    products = Product.objects.all()
    return render(request,'Ordernow.html',{'products': products})

def offers(request):
    return render(request, 'offers.html')

@login_required
def my_orders(request):
    return render(request, 'my_orders.html')

@login_required
def my_wishlist(request):
    return render(request, 'wishlist.html')

@login_required
def account_settings(request):
    return render(request, 'account_settings.html')

def feedbackform(request):
    if request.method == "POST":
        User_name = request.POST.get('User_name')
        Description = request.POST.get('Description')
        Rating = request.POST.get('Rating')
        User_Image = request.FILES.get('Selfie')
        if User_name and Description and Rating and User_Image:
            feedback = FeedbackForm(User_name=User_name, Description=Description, Rating=Rating,  Image=User_Image)
            feedback.save()
            messages.success(request, "FeedBackForm has successfully submited.")
        else:
            messages.error(request, "All fields are required!")
       
    return render(request,'Feedbackform.html')

    # return HttpResponse("this is Services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        if name and email and phone and desc:
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            contact.save()
            messages.success(request, "Your message has been sent")
        else:
            messages.error(request, "All fields are required!")
       
    return render(request, 'contact.html')
    
    # return HttpResponse("this is Contact page")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            

            # Optional: also save to your custom LoginRecord
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            record = LoginRecord(Username=username,password=password)
            record.save()

            user = authenticate(username=username, password=password)
            if user is not None:
            
                login(request, user)
                messages.success(request, "Logged in successfully.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Saves the User model

            
            # Save only the username (never the raw password)
            SignupRecord.objects.create(Username=user.username)

            messages.success(request, "Account created. You can log in now.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('/')

def icecream_list(request):
    flavour_data = {
        "name": "Vanilla",
        "description": "Classic and creamy ice cream.",
        "items": [
            {
                "id" : 6,
                "image": "vanila.jpg",
                "type": "Cup",
                "price": 50
            },
            {
                "id" : 7,
                "image": "vanilla1.jpg",
                "type": "Cone",
                "price": 60
            },
            {
                "id" : 8,
                "image": "vanilla2.jpg",
                "type": "Family Pack",
                "price": 150
            },
            {
                "id" : 9,
                "image": "vanila.jpg",
                "type": "Cup",
                "price": 50
            },
            {
                "id" : 10,
                "image": "vanilla1.jpg",
                "type": "Cone",
                "price": 60
            },
            {
                "id" : 11,
                "image": "vanilla2.jpg",
                "type": "Family Pack",
                "price": 150
            },
        ]
    }

    return render(request, "icecream_list.html", {
        "flavour": flavour_data
        # "items": flavour_data["items"]
        
    })

    # icecreams = IceCream.objects.all()
    # return render(request, 'icecream_list.html', {'icecreams': icecreams})

def icecream_detail(request, item_id):
    all_items =  [
            { "id": 0, "image": "5.jpg", "type": "Cup", "price": 50, "description": "Most Popular icecream in the world"},    # id 0
            { "id": 1, "image": "6.jpg", "type": "Cone", "price": 60},
            { "id": 2, "image": "7.jpg", "type": "Family Pack", "price": 150},
            { "id": 3, "image": "5.jpg", "type": "Cup", "price": 50},
            { "id": 4, "image": "6.jpg", "type": "Cone", "price": 60},
            { "id": 5, "image": "7.jpg", "type": "Family Pack", "price": 150},
            { "id": 6, "image": "vanila.jpg", "type": "Cup", "price": 50},
            { "id": 7, "image": "vanilla1.jpg", "type": "Cone", "price": 60},
            { "id": 8, "image": "vanilla2.jpg", "type": "Family Pack", "price": 150},
            { "id": 9, "image": "vanila.jpg", "type": "Cup", "price": 50},
            { "id": 10, "image": "vanilla1.jpg", "type": "Cone", "price": 60},         # id 10
            { "id": 11, "image": "vanilla2.jpg", "type": "Family Pack", "price": 150}, # id 11
            { "id": 12, "image": "Vanila.jpg", "type": "Cup", "price": 50},
            { "id": 13, "image": "Vanilla2.jpg", "type": "Cone", "price": 60},
            { "id": 14, "image": "Vanilla3.jpg", "type": "Family Pack", "price": 150},
            { "id": 15, "image": "Vanila.jpg", "type": "Cup", "price": 50},
            { "id": 16, "image": "Vanilla2.jpg", "type": "Cone", "price": 60},
            { "id": 17, "image": "Vanilla3.jpg", "type": "Family Pack", "price": 150}, # id 17
            { "id": 18, "image": "Chocolate.jpg", "type": "Cup", "price": 50},
            { "id": 19, "image": "Chocolate.jpg", "type": "Cone", "price": 60},
            { "id": 20, "image": "Chocolate.jpg", "type": "Family Pack", "price": 150}, # id 20
            { "id": 21, "image": "Chocolate.jpg", "type": "Cup", "price": 50},            # id 21
            { "id": 22, "image": "Chocolate.jpg", "type": "Cone", "price": 60},
            { "id": 23, "image": "Chocolate.jpg", "type": "Family Pack", "price": 150},
            { "id": 24, "image": "Strawberry.jpg", "type": "Cup", "price": 50},
            { "id": 25, "image": "Strawberry.jpg", "type": "Cone", "price": 60},
            { "id": 26, "image": "Strawberry.jpg", "type": "Family Pack", "price": 150},
            { "id": 27, "image": "Strawberry.jpg", "type": "Cup", "price": 50},
            { "id": 28, "image": "Strawberry.jpg", "type": "Cone", "price": 60},
            { "id": 29, "image": "Strawberry.jpg", "type": "Family Pack", "price": 150},
            { "id": 30, "image": "Mango.jpg", "type": "Cup", "price": 50},            # id 30
            { "id": 31, "image": "Mango.jpg", "type": "Cone", "price": 60},         # id 31
            { "id": 32, "image": "Mango.jpg", "type": "Family Pack", "price": 150},
            { "id": 33, "image": "Mango.jpg", "type": "Cup", "price": 50},
            { "id": 34, "image": "Mango.jpg", "type": "Cone", "price": 60},
            { "id": 35, "image": "Mango.jpg", "type": "Family Pack", "price": 150},
            { "id": 36, "image": "Butterscotch.jpg", "type": "Cup", "price": 50},
            { "id": 37, "image": "Butterscotch.jpg", "type": "Cone", "price": 60},
            { "id": 38, "image": "Butterscotch.jpg", "type": "Family Pack", "price": 150},
            { "id": 39, "image": "Butterscotch.jpg", "type": "Cup", "price": 50},
            { "id": 40, "image": "Butterscotch.jpg", "type": "Cone", "price": 60},                # id 40
            { "id": 41, "image": "Butterscotch.jpg", "type": "Family Pack", "price": 150},        # id 41
            { "id": 42, "image": "Pista.jpg", "type": "Cup", "price": 50},
            { "id": 43, "image": "Pista.jpg", "type": "Cone", "price": 60},
            { "id": 44, "image": "Pista.jpg", "type": "Family Pack", "price": 150},
            { "id": 45, "image": "Pista.jpg", "type": "Cup", "price": 50},
            { "id": 46, "image": "Pista.jpg", "type": "Cone", "price": 60},
            { "id": 47, "image": "Pista.jpg", "type": "Family Pack", "price": 150}, # id 47
        ]
    

    # try:
    #     item = flavour_data["items"][item_id]
    # except IndexError:
    #     return render(request, "404.html")

    # return render(request, "icecream_detail.html", {
    #     "item": item,
    #     "flavour_name": flavour_data["name"],
    # })
    item = next((x for x in all_items if x["id"] == item_id), None)
    if not item:
        return HttpResponseNotFound("Ice cream not found.")
    return render(request, "icecream_detail.html", {"item": item})

    # icecreams = IceCream.objects.all()
    # return render(request, "icecream_detail.html", {"icecreams": icecreams})


def category(request, flavour):
    # Dummy data for example – you can fetch from DB
    flavour_data = {
        "Vanilla": {
            # "images":[ "Vanila.jpg", "Vanilla1.jpg", "Vanilla2.jpg", "Vanilla3.jpg"], #2nd Way
            "description": "Classic and creamy Vanilla ice cream.",
              "items": [
                {
                    "id": 12,            
                    "image": "Vanila.jpg",
                    "type": "Cup",
                    "price": 50
                },
                {
                    "id": 13,
                    "image": "Vanilla2.jpg",
                    "type": "Cone",
                    "price": 60
                },
                {
                    "id": 14,
                    "image": "Vanilla3.jpg",
                    "type": "Family Pack",
                    "price": 200
                },
                {
                    "id": 15,
                    "image": "Vanila.jpg",
                    "type": "Cup",
                    "price": 50
                },
                {
                    "id": 16,
                    "image": "Vanilla2.jpg",
                    "type": "Cone",
                    "price": 60
                },
                {
                    "id": 17,
                    "image": "Vanilla3.jpg",
                    "type": "Family Pack",
                    "price": 200
                },
            ]
        },
        "Chocolate": {
           "description": "Rich chocolate flavor made from real cocoa.",
              "items": [
                {
                    "id": 18,
                    "image": "Chocolate.jpg",
                    "type": "Cup",
                    "price": 50
                },
                {
                    "id": 19,
                    "image": "Chocolate.jpg",
                    "type": "Cone",
                    "price": 60
                },
                {
                    "id": 20,
                    "image": "Chocolate.jpg",
                    "type": "Family Pack",
                    "price": 200
                },
                {
                    "id": 21,
                    "image": "Chocolate.jpg",
                    "type": "Cup",
                    "price": 50
                },
                {
                    "id": 22,
                    "image": "Chocolate.jpg",
                    "type": "Cone",
                    "price": 60
                },
                {
                    "id": 23,
                    "image": "Chocolate.jpg",
                    "type": "Family Pack",
                    "price": 200
                },
            ]
        },
        "Strawberry": {
           "description": "Fruity, fresh, and delightfully sweet.",
            "items": [
                {
                    "id": 24,
                    "image": "Strawberry.jpg",
                    "type": "Cup",
                    "price": 50
                },
                {
                    "id": 25,
                    "image": "Strawberry.jpg",
                    "type": "Cone",
                    "price": 60
                },
                {
                    "id": 26,
                    "image": "Strawberry.jpg",
                    "type": "Family Pack",
                    "price": 200
                },
                {
                    "id": 27,
                    "image": "Strawberry.jpg",
                    "type": "Cup",
                    "price": 50
                },
                {
                    "id": 28,
                    "image": "Strawberry.jpg",
                    "type": "Cone",
                    "price": 60
                },
                {
                    "id": 29,
                    "image": "Strawberry.jpg",
                    "type": "Family Pack",
                    "price": 200
                },
            ]
        },
        "Mango": {
           "description": "Rich tropical flavor in every bite.",
           "items": [
                {
                    "id": 30,
                    "image": "Mango.jpg",
                    "type": "Cup",
                    "price": 50
                },
                {
                    "id": 31,
                    "image": "Mango.jpg",
                    "type": "Cone",
                    "price": 60
                },
                {
                    "id": 32,
                    "image": "Mango.jpg",
                    "type": "Family Pack",
                    "price": 200
                },
                {
                    "id": 33,
                    "image": "Mango.jpg",
                    "type": "Cup",
                    "price": 50
                },
                {
                    "id": 34,
                    "image": "Mango.jpg",
                    "type": "Cone",
                    "price": 60
                },
                {
                    "id": 35,
                    "image": "Mango.jpg",
                    "type": "Family Pack",
                    "price": 200
                },
            ]
        },
        "Butterscotch": {
           "description": "Buttery caramel bliss with a crunch.",
            "items": [
                {
                    "id": 36,
                    "image": "Butterscotch.jpg",
                    "type": "Cup",
                    "price": 50
                },
                {
                    "id": 37,
                    "image": "Butterscotch.jpg",
                    "type": "Cone",
                    "price": 60
                },
                {
                    "id": 38,
                    "image": "Butterscotch.jpg",
                    "type": "Family Pack",
                    "price": 200
                },
                {
                    "id": 39,
                    "image": "Butterscotch.jpg",
                    "type": "Cup",
                    "price": 50
                },
                {
                    "id": 40,
                    "image": "Butterscotch.jpg",
                    "type": "Cone",
                    "price": 60
                },
                {
                    "id": 41,
                    "image": "Butterscotch.jpg",
                    "type": "Family Pack",
                    "price": 200
                },
            ]
        },
        "Pista": {
           "description": "Nutty, smooth, and irresistibly creamy.",
            "items": [
                {
                    "id": 42,
                    "image": "Pista.jpg",
                    "type": "Cup",
                    "price": 50
                },
                {
                    "id": 43,
                    "image": "Pista.jpg",
                    "type": "Cone",
                    "price": 60
                },
                {
                    "id": 44,
                    "image": "Pista.jpg",
                    "type": "Family Pack",
                    "price": 200
                },
                {
                    "id": 45,
                    "image": "Pista.jpg",
                    "type": "Cup",
                    "price": 50
                },
                {
                    "id": 46,
                    "image": "Pista.jpg",
                    "type": "Cone",
                    "price": 60
                },
                {
                    "id": 47,
                    "image": "Pista.jpg",
                    "type": "Family Pack",
                    "price": 200
                },
            ]
        },
        
    }   
    icecream = flavour_data.get(flavour)
    if not icecream:
        return render(request, "404.html")

    return render(request, "category.html", {
        "flavour": flavour,
        "icecream": icecream
    })

    # icecream = flavour_data.get(flavour, None)
    # if icecream is None:
    #     return render(request, "404.html")  # handle invalid flavour

    # return render(request, "category.html", {"flavour": flavour, "icecream": icecream})

def add_to_cart(request):
    icecream = IceCream.objects.all()
    return render(request, 'cart.html', {'icecream': icecream})

@csrf_exempt
def pay_now(request):
    if request.method == 'POST':
        
        # Save payment data here if using model
        # Payment.objects.create(method='Google Pay', amount=108, status='Paid')

        messages.success(request, 'Payment successful!')
        return redirect('/')  # or wherever you want
    return render(request, 'payment.html')  # fallback

# def add_to_cart(request):
#     cart = request.session.get('cart', {})
#      # add 1 quantity
#     request.session['cart'] = cart
#     return redirect('show_cart')

# def show_cart(request):
#     cart = request.session.get('cart', {})
#     items = []
#     total = 0
#     for item_id, qty in cart.items():
#         icecream = get_object_or_404(IceCream, pk=item_id)
#         subtotal = icecream.discounted_price * qty
#         total += subtotal
#         items.append({'icecream': icecream, 'quantity': qty, 'subtotal': subtotal})
#     return render(request, 'cart.html', {'items': items, 'total': total})