
from django.urls import path
from Product_app import views

urlpatterns = [
    path("",views.Product_details,name="Product_details"),
    path("add_product/",views.add_product,name="add_product"),
    path("product/<int:id>/", views.Product_pk, name="Product_pk"),
]