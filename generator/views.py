from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpRequest
from django.core.mail import send_mail

from datetime import datetime
from hashlib import sha1

from .forms import OrderCreateForm
from .models import Profile


def link_generator(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd['email']
            profile = Profile.objects.all().filter(email=email, active=True).first()
            if profile:
                profile.active = False
                profile.save()

            time = datetime.now().isoformat()
            plain = bytes(email + '\0' + time, 'utf-8')
            token = sha1(plain).hexdigest()

            profile = Profile(email=email, slug=token)
            profile.save()

            link = request.build_absolute_uri(reverse('view', args=[token]))

            subject = 'Your link'
            message = f"Dear {email},your link is {link}"

            send_mail(subject=subject,
                      message=message,
                      from_email='admin@magiclink.com',
                      recipient_list=[cd['email']])
            return render(request, 'generator/success.html',)

    else:
        form = OrderCreateForm()
        return render(request, 'generator/generator.html',
                      {'form': form})


def link_view(request, magic):
    profile = get_object_or_404(Profile, slug=magic, active=True)
    profile.count += 1
    profile.save()
    return render(request, 'generator/view.html',
                  {'profile': profile})
