from django.contrib import messages
from django.core.mail import send_mail
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
            send_mail(
                subject=f"Lagoon Solar: new Inquiry - {form.cleaned_data.get('subject')}",
                message=(
                    f"You have received a new message from the contact form: \n\n"
                    f"Name: {form.cleaned_data.get('name')}\n"
                    f"Email: {form.cleaned_data.get('email')}\n"
                    f"Subject: {form.cleaned_data.get('subject')}\n"
                    f"Message: {form.cleaned_data.get('message')}\n"
                ),
                from_email='noreply@lagoon.com',
                recipient_list=['Keniroyi050@gmail.com'],
                fail_silently=False,
            )
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
    
