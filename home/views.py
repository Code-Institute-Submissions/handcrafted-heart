from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

# Create your views here.
def contact(request):
    """
    Directs the customer to a contact me form
    """
   
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = settings.EMAIL_HOST_USER
            email_address = form.cleaned_data['email_address']
            message = form.cleaned_data['message']
            to_list = [email_address]
            send_mail(
                message,
                from_email,
                to_list,
                fail_silently=False)
            messages.success(
                request,
                """Your message was successfully sent,
                and you will be hearing from me soon!""")
        return redirect('products')
    context = {'contact_form': form}
    return render(request, 'contact.html', context)