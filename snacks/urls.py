from django.urls import path
from .views import snacksList, snacksDetail

urlpatterns = [
    path('', snacksList.as_view(), name='snacks_list'),
    path('<int:pk>/', snacksDetail.as_view(), name='snacks_detail'),
]