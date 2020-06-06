from django.urls import path, include

urlpatterns = [
    path('', include('apps.tv_shows.urls')),
]
