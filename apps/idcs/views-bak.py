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


# @api_view(['GET'])
# def api_root(request, *args, **kwargs):
#     return Response({
#         'idc': 'http://127.0.0.1:8000/idc_v2/'
#     })


from rest_framework.reverse import reverse
@api_view(['GET'])
def api_root(request, format=None, *args, **kwargs):
    return Response({
        'idc': reverse('idc-list', request=request, format=format)
    })


##########################  版本三   ############################
from rest_framework.views import APIView
from django.http import Http404


class IdcList(APIView):
    def get(self, request, format=None):
        queryset = Idc.objects.all()
        # print(queryset)
        serializer = IdcSerializer(queryset, many=True)
        # print(serializer)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IdcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class IdcDetail(APIView):
    def get_object(self, pk):
        try:
            return  Idc.objects.get(pk=pk)
        except Idc.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        idc = self.get_object(pk)
        serializer = IdcSerializer(idc)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        idc = self.get_object(pk)
        serializer = IdcSerializer(idc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        idc = self.get_object(pk)
        idc.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


##########################  版本四   ############################
from rest_framework import mixins, generics


class IdcList_V4(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class IdcDetail_V4(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


##########################  版本五   ############################
class IdcList_V5(generics.ListCreateAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer


class IdcDetail_V5(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer


##########################  版本六   ############################
from rest_framework import viewsets


class IdcListViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer


##########################  版本七   ############################
class IdcViewset_v7(viewsets.ModelViewSet):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer