from django.shortcuts import render

from .forms import EmailForm, JoinForm
from .models import Join


def home(request):
    #print (request.POST["email"], request.POST["email_2"])
    #Using regular django forms
    # form = EmailForm(request.POST or None)
    # if form.is_valid():
    #
    #     email = form.cleaned_data['email']
    #     new_join, created = Join.objects.get_or_create(email=email)
    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        email = form.cleaned_data['email']
        new_join_old, created = Join.objects.get_or_create(email=email)
        #new_join.save()
    context = {"form": form}
    template = "home.html"


    return render(request, template, context)
