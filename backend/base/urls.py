from django.urls import path, include
from .views import *


urlpatterns = [
    path('api/v1/category/', CategoryAPI.as_view()),
    path('api/v1/products/', ProductsAPI.as_view()),
    path('api/v1/product/<int:pk>', ProductAPI.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
