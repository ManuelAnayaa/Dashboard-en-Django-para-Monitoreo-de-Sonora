from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),  # Página principal
    path('api/data/', views.get_data_api, name='api_data'),  # API para el JS
]