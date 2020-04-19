from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'index.html',{})
def aboutus(request):
	return render(request,'about.html',{})
def service(request):
	return render(request,'service.html',{})
def portfolio(request):
	return render(request,'portfolio.html',{})
def blog(request):
	return render(request,'blog.html',{})
def contact(request):
	return render(request,'contact.html',{})
def blogitem(request):
	return render(request,'blog-item.html',{})
