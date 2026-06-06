from rest_framework import serializers 
from .models import Menu
from .models import Menu, Booking  # This targets your Menu model

class MenuSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Menu 
        # Explicitly listing out the fields from your Menu model schema
        fields = ['id', 'Title', 'Price', 'Inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'