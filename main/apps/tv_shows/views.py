from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TVshow

def index(request):
      context = {
            'shows': TVshow.objects.all()
      }
      return render(request, 'show_all.html', context)

def show_create(request):
      return render(request, 'create_show.html')

def create_show(request):
      errors = TVshow.objects.basic_validator(request.POST)
      if len(errors) > 0:
            for key, value in errors.items():
                  messages.error(request, value)
            return redirect('/shows/new')
      else :
            show = TVshow.objects.create(title=request.POST['title'], network=request.POST['network'], description=request.POST['description'], release_date=request.POST['release_date'])
            return redirect(f'/shows/{show.id}')

def show_one(request, show_id):
      context = {
            'show' : TVshow.objects.get(id=show_id)
      }
      return render(request, 'show_one.html', context)

def edit_show(request, show_id):
      context = {
            'show' : TVshow.objects.get(id=show_id)
      }
      return render(request, 'edit_show.html', context)

def update_show(request, show_id):
      errors = TVshow.objects.basic_validator(request.POST)
      if len(errors) > 0:
            for key, value in errors.items():
                  messages.error(request, value)
            return redirect(f'/shows/{show_id}/edit')
      else :
            show = TVshow.objects.get(id=show_id)
            show.title = request.POST['title']
            show.network = request.POST['network']
            show.release_date = request.POST['release_date']
            show.description = request.POST['description']
            show.save()
            return redirect(f'/shows/{show.id}')

def delete_show(request, show_id):
      TVshow.objects.get(id=show_id).delete()
      return redirect('/shows')