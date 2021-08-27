from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Hospital,Salesperson
from .serializers import HospitalSerializer,SalespersonSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def hospital_list(request):
    serializers = HospitalSerializer(data=request.data)

    if request.method == 'GET':
        hospital = Hospital.objects.all()
        serializers = HospitalSerializer(hospital,many=True)
        return Response(serializers.data)

    elif(request.method == 'POST'):
        # serializers = HospitalSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])

def hospital_list_detail(request,pk):
    try:
        hospital = Hospital.objects.get(pk=pk)
    except Hospital.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = HospitalSerializer(hospital)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = HospitalSerializer(hospital,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hospital.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# function based views for sales persons
@api_view(['GET','POST'])
def sales_view(request):

    if request.method == 'GET':
        user = request.user
        print("user name is:", user)
        sales = Salesperson.objects.filter(sales=user)


        return Response({'sales': SalespersonSerializer(sales, many=True).data, })

    elif (request.method == 'POST'):
        print(request.data)
        serializers = SalespersonSerializer(data=request.data)
        print(serializers)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)