from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from .models import Tea, Type
from .serializers import TeaSerializer, TypeSerializer

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

class TypeListCreate(generics.ListCreateAPIView):
  serializer_class = TypeSerializer

  def get_queryset(self):
    tea_id = self.kwargs['tea_id']
    print(tea_id)
    return Type.objects.filter(tea_id=tea_id)
  
  def perform_create(self, serializer):
    tea_id = self.kwargs['tea_id']
    tea = Tea.objects.get(id=tea_id)
    serializer.save(tea=tea)

class TypeListDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = TypeSerializer
  lookup_field = 'id'

  def get_queryset(self):
    tea_id = self.kwargs['tea_id']
    return Type.objects.filter(tea_id=tea_id)

