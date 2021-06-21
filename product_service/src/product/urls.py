from . import views
from django.urls import path

urlpatterns = [
    path('products/', views.InventoryListApi.as_view(), name='product-list')
]
