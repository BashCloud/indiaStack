from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import Crypto
import requests
import json
from models import Person
# Create your views here.
def index(request):
    template=loader.get_template('index.html')
    context={'login':'login'}
    if request.method == "POST":
        name = request.POST['name']
        addr = request.POST['addr']
        gender = request.POST['gender']
        age = request.POST['age']
        uidhash = request.POST['uid']
        headers = {"Content-type": "application/json"}
        url = "https://prod-26.southindia.logic.azure.com/workflows/f40afad470ac420f8dd399698ce3af41/triggers/request/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Frequest%2Frun&sv=1.0&sig=5CO1ms6IH1Oju_eZ5BbFqHP_rq7MwcD7mh9Hb2k3rDs"
        data = {'name': name, 'address': addr, 'gender': gender, 'age': age, 'uidhash': uidhash}
        person=Person(name=name,addr=addr,gender=gender,age=age,uidhash=uidhash)
        person.save()
        print data

        resp = requests.post(url, json=data,headers=headers)
        print resp
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context,request))