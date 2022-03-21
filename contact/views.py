from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from contact import forms


# Create your views here.
def contact(request):
    sent = False
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            # send form data to gmail
            data = {
                'name': cd['fullname'],
                'email': cd['email'],
                'subject': cd['subject'],
                'message': cd['message'],
            }
            message = '''
            New message:
            {}
            
            From: {} - {}
            '''.format(data['message'], data['name'],data['email'])
            # try:
            send_mail(data['subject'], message, '', ['icinecube@gmail.com',])
            # except Exception as e:
            #     # Ignore the smtp error message for showcase purpose
            #     print(e)

            return HttpResponseRedirect('/contact?sent=True')
    else:
        form = forms.ContactForm();
        if 'sent' in request.GET:
            sent = True

    return render(request, 'contact/contact.html', {'form': form, 'sent': sent})
