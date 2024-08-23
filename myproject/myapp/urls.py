from django.urls import path
from . import views

urlpatterns = [
    # path('products/',views.product_list)
    path('products/',views.ProductList.as_view()),
    path('products/<int:id>/',views.ProductDetails.as_view())
]
