from django.urls import path
from . import views

urlpatterns = [
    path('', views.shelterList, name="shelterList"),
    path('shelter/<int:pk>', views.shelterDetail, name="shelterDetail"),    
    # more to be added
    path("dog/<int:pk>", views.DogDetailView.as_view(), name="dogDetail"),
    path("dog/register", views.DogCreateView.as_view(), name="dogRegister")
]