from rest_framework import serializers
from .models import Booking, Menu, MenuItem
from django.contrib.auth.models import User

class BookingSerializer(serializers.ModelSerializer):
    """
    converts compound data types into JSON or XML format. 
    ModelSerializer: creates a serializer class from the Django model fields.
    """
    class Meta:
        model = Booking
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    """
    converts compound data types into JSON or XML format. 
    ModelSerializer: creates a serializer class from the Django model fields.
    """
    class Meta:
        model = Menu
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    """
    converts compound data types into JSON or XML format. 
    ModelSerializer: creates a serializer class from the Django model fields.
    """
    class Meta:
        model = MenuItem
        fields = '__all__'        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']