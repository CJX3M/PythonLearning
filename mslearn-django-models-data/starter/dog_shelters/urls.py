from django.urls import path
from . import views

urlpatterns = [
    path('', views.shelterList, name="shelterList"),
    path('shelter/<int:pk>', views.shelterDetail, name="shelterDetail"),
    # more to be added
]