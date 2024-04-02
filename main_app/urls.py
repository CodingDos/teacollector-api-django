from .views import Home, TeaList, TeaDetail
from django.urls import path

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('tea/', TeaList.as_view(), name='tea-list'),
  path('tea/<int:id>/', TeaDetail.as_view(), name='tea-detail'),
]