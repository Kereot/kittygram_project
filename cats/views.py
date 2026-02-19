from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cat
from .serializers import CatSerializer


# @api_view(['GET', 'POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cats = Cat.objects.all()
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data)


# class APICat(APIView):
#     def get(self, request):
#         cats = Cat.objects.all()
#         serializer = CatSerializer(cats, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def cat_detail(request, pk):
#     post = Cat.objects.get(id=pk)
#     if request.method == 'PUT' or request.method == 'PATCH':
#         serializer = CatSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     serializer = CatSerializer(post)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# class CatList(generics.ListCreateAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer
#
# class CatDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
