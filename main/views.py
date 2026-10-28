from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import ContactSubmissionForm
from .models import Questions

# Create your views here.
def home(request):
    questions = Questions.objects.filter(is_active=True)
    return render(request, 'index.html', {'questions': questions})

def error(request):
    return render(request, '404.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you. Your message has been received.')
            return redirect('contact')
    else:
        form = ContactSubmissionForm()
    return render(request, 'contact.html', {'form': form})

def feature(request):
    return render(request, 'feature.html')

def PHOTOCREDIT(request):
    return render(request, 'PHOTO-CREDITS.html')

def project(request):
    return render(request, 'project.html')

def quote(request):
    return render(request, 'quote.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')
    
