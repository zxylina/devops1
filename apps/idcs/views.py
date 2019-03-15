# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Idc
from django.shortcuts import render
from .serializers import IdcSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        kwargs.setdefault('content_type', 'application/json; charset=utf-8')
        content = JSONRenderer().render(data)
        super(JSONResponse, self).__init__(content=content, **kwargs)


##########################  版本一   ############################
def idc_list(request, *args, **kwargs):
    if request.method == 'GET':
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        return JSONResponse(serializer.data)
        # content = JSONRenderer().render(serializer.data)
        # return HttpResponse(content, content_type='application/json; charset=utf-8')
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        # print(data)
        serializer = IdcSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
            # content = JSONRenderer().render(serializer.data)
            # return HttpResponse(content, content_type='application/json; charset=utf-8')
    return HttpResponse('')


def idc_detail(request, pk, *args, **kwargs):
    try:
        idc = Idc.objects.get(pk=pk)
    except Idc.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = IdcSerializer(idc)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        content = JSONParser().parse(request)
        serializer = IdcSerializer(idc, data=content)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        idc.delete()
        return HttpResponse(status=204)

##########################  版本二   ############################
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def idc_list_v2(request, *args, **kwargs):
    if request.method == 'GET':
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        # return JSONResponse(serializer.data)
        return Response(serializer.data)
    elif request.method == 'POST':
        # print(request.data)
        serializer = IdcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return JSONResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def idc_detail_v2(request, pk, *args, **kwargs):
    try:
        idc = Idc.objects.get(pk=pk)
    except Idc.DoesNotExist:
        # return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = IdcSerializer(idc)
        # return JSONResponse(serializer.data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = IdcSerializer(idc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JSONResponse(serializer.data)
            return Response(serializer.data)
        # return JSONResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        idc.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)