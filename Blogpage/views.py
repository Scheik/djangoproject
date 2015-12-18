from django.shortcuts import render
from .models import posts

def blogpage(request):
	entries = posts.objects.all()[:100]
	return render(request, "blogpage.html",{ 'posts' : entries })
