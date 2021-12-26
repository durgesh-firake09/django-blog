from django.shortcuts import redirect, render, HttpResponse
from home.models import Contact, Post, SignedUp
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def checkLoggedIn(request):
    try:
        if request.session["loggedIn"] == True:
            return True
        else:
            return False

    except Exception as e:
        return False


def returnUser(request):
    user = SignedUp.objects.filter(email=returnUserEmail(request)).first()
    if user == None:
        return "None"
    return user


def returnUserEmail(request):
    try:
        if request.session["loggedIn"] == True:
            return request.session["userEmail"]
        else:
            return "None"
    except Exception as e:
        return "None"


def returnUserName(user):
    if user == "None":
        return "None"
    return user.name


def index(request):

    context = {
        "loggedIn": checkLoggedIn(request),
        "userName": returnUserName(returnUser(request))
    }
    print()
    return render(request=request, template_name="index.html", context=context)


def about(request):
    context = {
        "loggedIn": checkLoggedIn(request),
        "userName": returnUserName(returnUser(request))
    }
    return render(request, "aboutUs.html", context=context)


def contact(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # print(f"{name} : {email}\n{phone}\nMessage : {message}")

        if((len(name) > 5) and (len(phone) == 10)):
            contact = Contact(name=name, email=email,
                              phone=phone, message=message, date=datetime.today())
            contact.save()
        else:
            print("Contact Unsuccessfull")

    context = {
        "loggedIn": checkLoggedIn(request),
        "userName": returnUserName(returnUser(request))
    }
    return render(request, "contactUs.html", context=context)


def browsePosts(request):
    posts = Post.objects.all()
    context = {
        "loggedIn": checkLoggedIn(request),
        "posts": posts,
        "userName": returnUserName(returnUser(request))
    
    }
    return render(request, "allBlogs.html", context=context)


def signUp(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if((len(name) > 5) and (len(phone) == 10) and (password1 == password2)):
            checkUserEmail = SignedUp.objects.filter(email=email).first()
            if checkUserEmail == None:
                if(len(password1) < 5):
                    print("Please Create a Strong Password")
                    # TODO : Django message framework here
                    return render(request, "signUp.html")
                else:
                    hashed_password = make_password(password1)
                    user = SignedUp(name=name, email=email, dob=dob,
                                    phone=phone, password=hashed_password)
                    user.save()
                    return redirect("/user/login/?redirected_from=sign_up_page")
            else:
                print("User Already Exists")

    context = {
        "loggedIn": checkLoggedIn(request),
        "userName": returnUserName(returnUser(request))
    }
    return render(request, "signUp.html", context=context)


def login(request):
    redirected_from = ""
    if len(request.GET) != 0:
        try:
            redirected_from = request.GET['redirected_from']
        except Exception as e:
            pass

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = SignedUp.objects.filter(email=email).first()
        if user == None:
            print("User Didn't Exist")
        else:
            password_checked = check_password(
                password=password, encoded=user.password)
            if(password_checked):
                print("Password Matched")
                request.session["userEmail"] = email
                request.session["loggedIn"] = True
                return redirect("/")

            else:
                print("Password Don't Matched")
    context = {
        "redirected_from": redirected_from,
        "loggedIn": checkLoggedIn(request),
        "userName": returnUserName(returnUser(request))
    }

    return render(request, "login.html", context=context)


def resetPassword(request):
    context = {
        "loggedIn": checkLoggedIn(request),
        "userName": returnUserName(returnUser(request))
    }
    return render(request, "resetPassword.html", context=context)


def viewPost(request, sno):
    post = Post.objects.filter(sno=sno).first()
    context = {
        "loggedIn": checkLoggedIn(request),
        "post": post,
        "userName": returnUserName(returnUser(request))

    }
    return render(request, "postTemplate.html", context=context)
