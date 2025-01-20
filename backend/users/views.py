from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer
# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User registered succesfuly'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        username=request.data.get('username')
        email=request.data.get('email')
        password=request.data.get('password')
        user=authenticate(username=username, email=email, password=password)
        if user:
            login(request, user)
            return Response({'message':'User logged in succesfuly'}, status=status.HTTP_200_OK)
        return Response({'message':'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)