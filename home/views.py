from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request=request, template_name="index.html")


def about(request):
    return render(request, "aboutUs.html")


def contact(request):
    return render(request, "contactUs.html")


def browsePosts(request):
    return render(request, "allBlogs.html")


def signUp(request):
    return render(request, "signUp.html")


def login(request):
    return render(request, "login.html")


def resetPassword(request):
    return render(request, "resetPassword.html")


def viewPost(request, sno):
    post = {
        "sno": 1,
        "title": "This is The First Post",
        "date": "09/10/2003",
        "body": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Molestias mollitia porro adipisci repudiandae debitis voluptates, consequuntur, fuga reiciendis minima architecto minus aliquam dolorum dolores iure officiis magnam neque? Fugit consectetur sit minima, nobis dolorem, provident facere aperiam ex ut animi deserunt, corrupti quaerat in voluptas perspiciatis eveniet quis esse molestiae officia officiis? Nemo at et pariatur in dicta impedit nam nulla quas sunt incidunt culpa officia reiciendis, porro dolorem rem sint! Hic, consequatur sapiente. Dignissimos harum ipsum soluta rerum debitis quos laboriosam, explicabo modi cumque! Dolor enim autem, nobis natus deserunt eaque quod ut dolores quam assumenda quisquam nulla eveniet."
    }
    return render(request, "postTemplate.html", context=post)
