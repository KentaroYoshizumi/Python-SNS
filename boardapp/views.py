from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def signupfunc(request):
    object = User.objects.get(username='tanaka')
    print(object.email)
    if request.method == "POST":
        print("This is post method.")
    else:
        print("This is not post method.")
    return render(request, 'signup.html', {'some':100})
