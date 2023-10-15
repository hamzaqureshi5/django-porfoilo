from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    context={"name":"Hamza Qureshi",
             "bottom_line": "Engineer"}
#    return render(request,"index.html",{"data":context})
    return render(request,"index.html",context)
    
def about(request):
    return render(request,"education.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")
