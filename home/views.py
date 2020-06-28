from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Contact, Newsletter, Image

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {
        'projects' : projects,
    }
    return render(request, 'home/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        ref = Contact(name = name, email = email, subject = subject, message = message)
        messages.success(request, 'Your message has been succesfully recieved by us. We will contact you ASAP!!')
        ref.save()
    return redirect('/')

def newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']
        ref = Newsletter(email = email)
        ref.save()
        messages.success(request, 'You have been succesfully added to the list!!')
    return redirect('/')


def detail(request, pk):
    project = Project.objects.filter(pk = pk).first()
    context = {
        'project' : project,
    }
    return render(request, 'home/portfolio-details.html', context)