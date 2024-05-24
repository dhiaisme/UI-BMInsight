
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def appoinment(request):
    return render(request, 'appoinment.html')

def blog_sidebar(request):
    return render(request, 'blog-sidebar.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def example(request):
    return render(request, 'dataset-example.html')

def contact(request):
    return render(request, 'contact.html')

def department_single(request):
    return render(request, 'department-single.html')

def department(request):
    return render(request, 'department.html')

def doctor_single(request):
    return render(request, 'doctor-single.html')

def doctor(request):
    return render(request, 'doctor.html')

def documentation(request):
    return render(request, 'documentation.html')

def index_copy(request):
    return render(request, 'index-copy.html')

def services(request):
    return render(request, 'service.html')
