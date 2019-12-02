from django.shortcuts import render
#from gallery.models import Gallery

def home(request):
    #gallerys = Gallery.description
    #return render(request,'home.html',{'gallerys':gallerys})
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')