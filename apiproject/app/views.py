from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.views.generic import TemplateView
from django.views import View
import json
from app.models import register

def index(request):
    return render(request, 'home.html')

def tes(request):
    return render(request, 'test.html')

def article(request):
    return render(request, 'article_detail.html')

class IdealWeight(View):

    def post(heightdata):
        #import pdb; pdb.set_trace(loads)
        try:    
            height=json.loads(heightdata.body)
            weight=str(height*10)
            return JsonResponse("Ideal weight should be:"+weight+" kg",safe=False)
        except ValueError as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

class temp(APIView):

    def get(self, request):
        users = register.objects.all().values()
        #user_list = list(reg)
        return JsonResponse(list(users), safe=False)

    def post(self):
        pass

    