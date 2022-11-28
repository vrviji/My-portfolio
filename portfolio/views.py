from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def skills(request):
    return render(request,'skills.html')

def experience(request):
    return render(request,'experience.html')

def award(request):
    return render(request,'award.html')

def contact(request):
    return render(request,'contact.html')