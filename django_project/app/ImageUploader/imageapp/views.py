# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import ImageUploadForm
from .models import UploadedImage
from .forms import SignupForm
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("password2")
        # print(uname, email, pass1, pass2)
        if pass1 != pass2:
            return HttpResponse("Your password not match!!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            # return HttpResponse("User has been created successfully!!!")
            return redirect('login')
    return render(request, 'signup.html' )


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload_image')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request, 'login.html')
    
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save(commit=False)
            uploaded_image.user = request.user
            uploaded_image.save()
         
            return redirect('image_gallery')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def image_gallery(request):
    last_uploaded_image_type = UploadedImage.objects.filter(user=request.user).order_by('-uploaded_at').first()
    if last_uploaded_image_type:
        last_image_type = last_uploaded_image_type.image_type
    else:
        last_image_type = None

    imag   = UploadedImage.objects.filter(user=request.user)
    return render(request, 'image_gallery.html', {'imag': imag  , 'last_image_type': last_image_type})