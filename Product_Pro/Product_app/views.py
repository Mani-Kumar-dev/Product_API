from django.http import JsonResponse
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from Product_app.models import Products
from Product_app.serializers import ProductSerializer
from django.contrib import messages
# Create your views here.
@api_view(['GET'])
def Product_details(request):
    pro = Products.objects.all()
    serializer = ProductSerializer(pro,many=True)
    context = {'data':serializer.data}
    return render(request,"product.html",context)

@api_view(['GET'])
def Product_pk(request, id):
    try:
        product = Products.objects.get(pk=id)
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)
    except Products.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

@api_view(['POST', 'GET'])
def add_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect("Product_details")
        else:
            return render(request, 'product.html', {'errors': serializer.errors})
    return render(request, "product.html")
