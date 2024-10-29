from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from products.models import Product, Image
from products.productAPI.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['post'])
    def upload_images(self, request, pk=None):
        #retrieve an instance of the product with pk
        product = self.get_object()
        #get the images as list of files (name, size, contentn_type..) from the request
        files = request.FILES.getlist('images') 
        
        for file in files:
            #create an instance of the Image model
            Image.objects.create(product=product, image=file)
        
        return Response({"message": "Images uploaded successfully"}, status=status.HTTP_201_CREATED)