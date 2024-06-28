from django.shortcuts import render
from .models import Blog
# Create your views here.

def blog_view(request):
    blog = Blog.objects.all()
    context = {'blog':blog}

    return render(request,'index.html',context)

def blog_detail_view(request,id):
    blog = Blog.objects.get(id=id)
    context = {'blog':blog}

    return render(request,'detail.html',context)

def contact_views(request):
    if request.method == 'POST' :
        print("Siz Post request yubordigiz")
    return render(request,'contact.html')
