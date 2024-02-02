from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import *
from .serializer import PostSerializer
from rest_framework import status


# Create your views here.

def home_page(request: Request):
    response = {"message": "Hello"}
    return JsonResponse(response)


@api_view(['GET'])
def get(request: Request):
    post = Crud.objects.all()
    serializer = PostSerializer(post, many=True)
    response = {"message": "Posts are gotten successfully",
                "data": serializer.data}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create(request:Request):
    if __name__ == '__main__':
        if request.method == "POST":
            data = request.data
            serializer = PostSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                response = {"message" : "New post created",
                            "data" : serializer.data}
                return Response(data=response , status=status)
            return Response(data=serializer.errors ,status=status)


@api_view(['DELETE'])
def delete_post(request: Request, pk: int):
    post = get_object_or_404(Crud, pk=pk)
    post.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['UPDATE'])
def update(request:Request, pk : int):
    post = get_object_or_404(Crud, pk=pk)
    if request.method == 'POST':
        data = request.data
        serializer = PostSerializer(instance=post, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "Post updated",
                        'data': serializer.data}
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status)
