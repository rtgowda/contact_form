from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact message to the database
            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()  # Create an empty form instance
    return render(request, 'contact/contact_form.html', {'form': form})

def contact_success(request):
    return render(request, 'contact/contact_success.html')

def contact_messages(request):
    messages = ContactMessage.objects.all()  # Retrieve all contact messages
    return render(request, 'contact/contact_messages.html', {'messages': messages})