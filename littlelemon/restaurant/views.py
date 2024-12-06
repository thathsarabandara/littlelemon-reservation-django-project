from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import permission_classes , api_view
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from .models import Booking, Menu
from .serializers import bookingSerializer, menuSerializer  # Make sure the serializers are imported correctly

class BookingView(APIView):
    
    def get(self, request):
        # Fetch all bookings
        items = Booking.objects.all()
        # Serialize the data
        serializer = bookingSerializer(items, many=True)
        # Return the serialized data as a Response
        return Response(serializer.data)

class MenuView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class= menuSerializer

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

def home(request):
    return render(request, 'index.html')