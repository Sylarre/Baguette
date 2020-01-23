from django.urls import path
from .views import (
    RetetaListView,
    RetetaDetailView,
    RetetaCreateView,
    RetetaUpdateView,
    RetetaDeleteView
)
from . import views

urlpatterns = [
    path('', RetetaListView.as_view(), name='retete-acasa'),
    path('reteta/<int:pk>/', RetetaDetailView.as_view(), name='reteta-detail'),
    path('reteta/nou/', RetetaCreateView.as_view(), name='reteta-create'),
    path('reteta/<int:pk>/actualizare/', RetetaUpdateView.as_view(), name='reteta-update'),
    path('reteta/<int:pk>/stergere/', RetetaDeleteView.as_view(), name='reteta-delete'),
    path('despre/', views.despre, name='retete-despre'),
]