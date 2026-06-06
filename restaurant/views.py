from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

from django.http import HttpResponse

def sayHello(request):
 return HttpResponse('Hello World')

def index(request):
 return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView): 
    queryset = Menu.objects.all() 
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):     
    queryset = Menu.objects.all() 
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    # This line completely locks the endpoint!
    permission_classes = [IsAuthenticated]  
    
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
