from django.db import models

# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    message = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.name} - {self.email}"


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.TextField()
    posted_by = models.CharField(default="Admin", max_length=20)
    body = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.title


class SignedUp(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    dob = models.DateField()
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name} - {self.email}"


class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    user_posted = models.ForeignKey(SignedUp,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment_body = models.TextField()
    posted_on = models.DateField()

    def __str__(self) -> str:
        return f"{self.user_posted.name} - {self.comment_body[0:100]}..."
