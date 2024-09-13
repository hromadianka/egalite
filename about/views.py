from django.shortcuts import render
from .models import AboutUs, ResourceLink, Store

# Create your views here.

def about_view(request):
    about = AboutUs.objects.first()
    resource_links = ResourceLink.objects.all()
    stores = Store.objects.all()
    
    context = {
        'about': about,
        'resource_links': resource_links,
        'stores': stores,
    }
    
    return render(request, 'about/about.html', context)