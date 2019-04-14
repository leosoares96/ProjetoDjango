from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
	return render(request,"cadastro.html")
def contato(request):
	return render(request,"contato.html")
def index(request):
	return render(request,"index.html")
def login(request):
	return render(request,"login.html")
def sobre(request):
	return render(request,"sobre.html")
