from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from .forms import customerform
# Create your views here.
def index(request):
    return render (request ,"index.html")
    
def about(request):
    return render(request, "about.html")

def contacts(request):
    return render(request, "contacts.html")

def products(request):
    return render (request ,"products.html")

def services(request):
    return render (request ,"services.html")

def test(request):
    return render(request, "test.html")

def story(request):
    return render (request ,"story.html")  
  
def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('sm-meet', 'w3school.com')  
    return response  

def getcookie(request):  
    tutorial  = request.COOKIES['sm-meet']  
    return HttpResponse("Django project @: "+  tutorial);

def forms(request):
    form  = customerform() 
    if request.method=='POST':
        form = customerform(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'forms.html',context)


'''def contactdetails(request):
    if request.method=='POST':
        form=snippetform(request.POST)
        if form.is_valid():
            Name=form.cleaned_data['Name']
            Email=form.cleaned_data['Email']        
            print(Name, Email)

    form=snippetform(request.POST)
    return render(request,"forms.html",{'form':form})
'''
