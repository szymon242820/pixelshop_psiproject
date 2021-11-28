from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, OrderSerializer, PixelArtSerializer
from pixelshop.models import User, Order, PixelArt

# main api view
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'User -> List': '/user/user-list/',
        'User -> DetailView': '/user/user-detail/<str:pk>/',
        'User -> Create': '/user/user-create/',
        'User -> Update': '/user/user-update/<str:pk>/',
        'User -> Delete': '/user/user-delete/<str:pk>/',
        'PixelArt -> List': '/pixelart/pixelart-list/',
        'PixelArt -> DetailView': '/pixelart/pixelart-detail/<str:pk>/',
        'PixelArt -> Create': '/pixelart/pixelart-create/',
        'PixelArt -> Update': '/pixelart/pixelart-update/<str:pk>/',
        'PixelArt -> Delete': '/pixelart/pixelart-delete/<str:pk>/',
        'Order -> List': '/order/order-list/',
        'Order -> DetailView': '/order/order-detail/<str:pk>/',
        'Order -> Create': '/order/order-create/',
        'Order -> Update': '/order/order-update/<str:pk>/',
        'Order -> Delete': '/order/order-delete/<str:pk>/'
    }
    return Response(api_urls)

# --------------- user section ----------------------- 
@api_view(['GET'])
def userList(request):
    """UserList Rest View."""
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def userDetail(request, pk):
    """UserDetail Rest View."""
    try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response("Nie istnieje User z takim kluczem głównym.")
    

@api_view(['POST'])
def userCreate(request):
    """UserCreate Rest View."""
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def userUpdate(request, pk):
    """UserUpdate Rest View."""
    try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response("Nie istnieje User z takim kluczem głównym.")


@api_view(['DELETE'])
def userDelete(request, pk):
    """UserUpdate Rest View."""
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return Response("User został usunięty poprawnie!")
    except User.DoesNotExist:
        return Response("Nie istnieje User z takim kluczem głównym.")


# --------------- order section ----------------------- 
@api_view(['GET'])
def orderList(request):
    """OrderList Rest View."""
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def orderDetail(request, pk):
    """OrderDetail Rest View."""
    try:
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)
    except Order.DoesNotExist:
        return Response("Nie istnieje Order z takim kluczem głównym.")


@api_view(['POST'])
def orderCreate(request):
    """OrderCreate Rest View."""
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def orderUpdate(request, pk):
    """OrderUpdate Rest View."""
    try:
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(instance=order, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Order.DoesNotExist:
        return Response("Nie istnieje Order z takim kluczem głównym.")


@api_view(['DELETE'])
def orderDelete(request, pk):
    """OrderUpdate Rest View."""
    try:
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response("Zamówienie zostało usunięte poprawnie!")
    except Order.DoesNotExist:
        return Response("Nie istnieje Order z takim kluczem głównym.")


# --------------- pixelart section ----------------------- 
@api_view(['GET'])
def pixelartList(request):
    """PixelArtList Rest View."""
    pixelarts = PixelArt.objects.all()
    serializer = PixelArtSerializer(pixelarts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def pixelartDetail(request, pk):
    """PixelArtDetail Rest View."""
    try:
        pixelart = PixelArt.objects.get(pk=pk)
        serializer = PixelArtSerializer(pixelart, many=False)
        return Response(serializer.data)
    except PixelArt.DoesNotExist:
        return Response("Nie istnieje PixelArt z takim kluczem głównym.")


@api_view(['POST'])
def pixelartCreate(request):
    """PixelArtCreate Rest View."""
    serializer = PixelArtSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def pixelartUpdate(request, pk):
    """PixelArtUpdate Rest View."""
    try:
        pixelart = PixelArt.objects.get(pk=pk)
        serializer = PixelArtSerializer(instance=pixelart, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except PixelArt.DoesNotExist:
        return Response("Nie istnieje PixelArt z takim kluczem głównym.")


@api_view(['DELETE'])
def pixelartDelete(request, pk):
    """PixelArtUpdate Rest View."""
    try:
        pixelart = PixelArt.objects.get(pk=pk)
        pixelart.delete()
        return Response("PixelArt został usunięty poprawnie!")
    except PixelArt.DoesNotExist:
        return Response("Nie istnieje PixelArt z takim kluczem głównym.")