from django.shortcuts import render

def index(request):
	return render(request, "index.html")

def dress(request):
	return render(request,"dress.html")

def signup(request):
	return render(request,"signup.html")

def register(request):
	return render(request,"register.html")

def AdminDashboard(request):
	return render(request,"Admin_Dashboard.html")