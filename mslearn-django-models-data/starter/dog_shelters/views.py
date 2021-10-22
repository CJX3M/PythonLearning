from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.
def shelterList(request):
    shelters = models.Shelter.objects.all()
    context = { 'shelters': shelters }
    return render(request, 'shelterList.html', context)

def shelterDetail(request, pk):
    shelter = models.Shelter.objects.get(pk=pk)
    context = { 'shelter': shelter }
    return render(request, 'shelterDetail.html', context)