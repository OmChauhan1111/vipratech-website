from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from .models import JobApplication


# Create your views here.
def index(request):
    context = {
        'variable': "This is sent from views.py",
    }
    return render(request, 'index.html', context)

    # return HttpResponse("Welcome to the home page!")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("Welcome to the about page!")

def contact(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            focus = request.POST.get('focus')
            roadmap = request.POST.get('roadmap')

            # Save the contact information to the database
            contact = Contact(name=name, email=email, focus=focus, roadmap=roadmap)
            contact.save()
            messages.success(request, 'Your message has been sent successfully!')



        return render(request, 'contact.html')

    # return HttpResponse("Welcome to the contact page!")

def services(request):
         return render(request, 'services.html')

    # return HttpResponse("Welcome to the services page!")

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import JobApplication

def career(request):
    if request.method == "POST":

        print("POST HIT")   # Debug line

        JobApplication.objects.create(
            fullname=request.POST.get('fullname'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            role=request.POST.get('role'),
            experience=request.POST.get('experience'),
            expected_salary=request.POST.get('salary'),
            github=request.POST.get('github'),
            linkedin=request.POST.get('linkedin'),
            about=request.POST.get('about'),
            resume=request.FILES.get('resume')
        )

        messages.success(request, "Application submitted successfully ")
        return redirect('/career')

    return render(request, 'career.html')