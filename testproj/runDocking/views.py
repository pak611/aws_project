from http.client import responses
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
#from rest_framework.views import APIView
#from rest_framework.response import Response
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from .forms import UploadPdbForm
from .models import docking_input

#from rest_framework.response import Response
import pandas as pd

import csv


# Create your views here.

class home(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = UploadPdbForm(request.POST, request.FILES)
            if form.is_valid():
                    print('input is valid')
                    option1 = form.cleaned_data.get('option1')
                    option2 = form.cleaned_data.get('option2')
                    option3 = form.cleaned_data.get('option3')
                    option4 = form.cleaned_data.get('option4')
                    title = form.cleaned_data['title']
                    pdbfile = form.cleaned_data['pdb_file']

                    alert_message = {
                        'status': True,
                        'message': 'Successfully saved the file'
                    }

                    context = {
                        'alert_data': alert_message,
                        'form': form,
                        'pdb_file': docking_input.objects.all
                    }

                    # create the instance
                    ins = docking_input(title = title, pdbfile = pdbfile, option1 = option1, option2 = option2, option3 = option3, option4 = option4)
                    ins.save
                    print('data has been written to db')

            else:
                alert_message = {
                    'status': False,
                    'message': 'Form data is invalid. Please check if your image / title is repeated'
                }

                form = UploadPdbForm()
                context = {
                    'alert_data': alert_message,
                    'form': form,
                    'images': docking_input.objects.all
                }
        else:

            form = UploadPdbForm()
            context = {
                'form': form,
                'images': docking_input.objects.all
            }
        return render(request, 'mainPageDir/mainpage.html', context = context)
        
    
class testView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mainPageDir/testpage.html')
        

    def post(self,request):
      return HttpResponse('Class based view')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         