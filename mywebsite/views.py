from django.shortcuts import render,HttpResponseRedirect
from mywebsite.forms import contactform,newsletterform
from django.contrib import messages
# Create your views here.
def index_view(request):
    return render(request,'website/index.html')
def about_view(request):
    return render(request,'website/about.html')
def contact_view(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            contact=form.save(commit=False)
            contact.name='unknown'
            contact.save()
            messages.add_message(request,messages.SUCCESS,'your submit is successful')
        else:
           messages.add_message(request,messages.ERROR,'your submit is not successful') 
    else:
        form=contactform()    
    return render(request,'website/contact.html',{'form':form})
def newsletter_view(request):
    if request.method=='POST':
        form=newsletterform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/') 
        else :
            print(form.errors)
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')   
def coming_view(request):
    return render(request,'website/coming_soon.html')