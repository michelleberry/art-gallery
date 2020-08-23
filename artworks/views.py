
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import collection, artPiece


def index(request):
    collection_list = collection.objects.all()
    template = loader.get_template('artworks/index.html')
    context = {
        'collection_list': collection_list,
    }
    return HttpResponse(template.render(context, request))

def about_me(request):
    return render(request, 'artworks/about_me.html', {})

def collection_index(request, pk):
    thisCollection = collection.objects.get(pk=pk)
    artPieces = thisCollection.artpiece_set.all()
    template = loader.get_template('artworks/collection_index.html')
    context = {
        'artPieces': artPieces,
        'thisCollection': thisCollection
    }
    return HttpResponse(template.render(context,request))

def art_details(request, collection_id, art_id):
    thisCollection = collection.objects.get(pk=collection_id)
    artPiece = thisCollection.artpiece_set.get(pk=art_id)
    template = loader.get_template('artworks/art_details.html')
    context = {
        'artPiece': artPiece,
        'thisCollection': thisCollection
    }
    return HttpResponse(template.render(context,request))