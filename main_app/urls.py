from .views import Home, TeaList, TeaDetail, TypeListCreate, TypeListDetail
from django.urls import path

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('tea/', TeaList.as_view(), name='tea-list'),
  path('tea/<int:pk>/', TeaDetail.as_view(), name='tea-detail'),
  path('tea/<int:pk>/type/', TypeListCreate.as_view(), name='type-list-create'),
  path('tea/<int:pk>/type/<int:tea_id>/', TypeListDetail.as_view(), name='type-list-detail'),
]