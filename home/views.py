from django.shortcuts import redirect, render, HttpResponse
from home.models import Comment, Contact, Post, SignedUp
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

        if password1!=password2:
            messages.error(request,"Passwords Do Not Match.")
            return redirect("/user/sign-up/")

        if((len(name) > 5) and (len(phone) == 10) and (password1 == password2)):
            checkUserEmail = SignedUp.objects.filter(email=email).first()
            if checkUserEmail == None:
                if(len(password1) < 5):
                    print("Please Create a Strong Password")
                    messages.error(request,"Please Create a Strong Password")
                    return redirect("/user/sign-up/")
                else:
                    hashed_password = make_password(password1)
                    user = SignedUp(name=name, email=email, dob=dob,
                                    phone=phone, password=hashed_password)
                    user.save()
                    messages.success(request,"Your Account has been cerated Successfully. You Can Now Login.")
                    return redirect("/user/login/")
            else:
                messages.error(request,"User Already Exists with This Email ID")
        if len(name)<=5:
            messages.error(request,"Name should be more than 5 Characters.")
            return redirect("/user/sign-up/")
        if len(phone)<10:
            messages.error(request,"Phone Number should be of 10 Digits")
            return redirect("/user/sign-up/")

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
            messages.error(request, "Invalid Credentials")
            return redirect("/user/login/")
        else:
            password_checked = check_password(
                password=password, encoded=user.password)
            if(password_checked):
                print("Password Matched")
                request.session["userEmail"] = email
                request.session["loggedIn"] = True
                messages.success(request, f"Logged in as {user.name}")
                return redirect("/")

            else:
                messages.error(request,"Invalid Credentials")
                return redirect("/user/login/")
    context = {
        "redirected_from": redirected_from,
        "loggedIn": checkLoggedIn(request),
        "userName": returnUserName(returnUser(request))
    }

    return render(request, "login.html", context=context)


def logout(request):
    if checkLoggedIn(request):
        # request.session["loggedIn"] = False
        request.session.flush()
        messages.info(request,"Logged Out Successfully")
    return redirect('/')


def resetPassword(request):
    userIdentified = False
    user = None
    if request.method == "POST":

        if request.POST["reset_now"] == "No":
            email = request.POST['email']
            phone = request.POST['phone']
            dob = request.POST['dob']

            user = SignedUp.objects.filter(email=email).first()
            if((user.phone == phone) and (str(user.dob) == dob)):
                userIdentified = True
            else:
                messages.error(request,"User Not Found")
                return redirect("/user/reset-password/")
        elif request.POST["reset_now"] == "Yes":
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            target_user_email = request.POST['user']
            target_user = SignedUp.objects.filter(
                email=target_user_email).first()
            if password2 == password1:
                hashed_password = make_password(password1)
                target_user.password = hashed_password
                target_user.save()
                messages.success(request,"Password Reset Successfully. You Can Now Login.")
                return redirect('/user/login/')
            else:
                messages.error(request,"Password Entered and Confirmed Password do not Match. Please try Again.")
                return redirect('/user/reset-password/')

    context = {
        "loggedIn": checkLoggedIn(request),
        "userName": returnUserName(returnUser(request)),
        "userIdentified": userIdentified,
        "user": user
    }
    return render(request, "resetPassword.html", context=context)


def viewPost(request, sno):
    post = Post.objects.filter(sno=sno).first()
    if request.method == "POST":
        comment = Comment(post=post, user_posted=returnUser(
            request), posted_on=datetime.today(), comment_body=request.POST['comment'])
        comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "loggedIn": checkLoggedIn(request),
        "post": post,
        "userName": returnUserName(returnUser(request)),
        "comments": comments
    }
    return render(request, "postTemplate.html", context=context)
