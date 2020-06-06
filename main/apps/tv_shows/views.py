from django.shortcuts import render

def index(request):
      return render(request, 'index.html')

def show_create(request):
      return render(request, 'create_show.html')