from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from .models import Tea
from .serializers import TeaSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the teacollector api home route!'}
    return Response(content)
  
class TeaList(generics.ListCreateAPIView):
  queryset = Tea.objects.all()
  serializer_class = TeaSerializer

class TeaDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Tea.objects.all()
  serializer_class = TeaSerializer
  lookup_field = 'id'