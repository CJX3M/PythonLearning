from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
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

# Create generic views
class DogDetailView(generic.DetailView):
    model = models.Dog
    template_name = "dogDetail.html"
    context_object_name = "dog"

class DogCreateView(generic.CreateView):
    model = models.Dog
    template_name = "dogForm.html"
    fields = ["name", "description", "shelter"]

class DogUpdateView(generic.UpdateView):
    model = models.Dog
    template_name = "dogForm.html"
    fields = ["name", "description", "shelter"]

class DogDeleteView(generic.DeleteView):
    model = models.Dog
    success_url = reverse_lazy('dogDetail')

