from django.shortcuts import render
from .serializers import SignupSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user
# Create your views here.

class SignupView(generics.GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'User created successfully',
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request:Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {
                'message' : 'Login succesful',
                'token':tokens
            }
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={'message': 'Invalid credentials'}, status=status)

    def get(self, request:Request, *args , **kwargs):
        content = {
            'user' : str(request.user),
            'auth' : str(request.auth),
        }
        return Response(data=content, status=status.HTTP_200_OK)