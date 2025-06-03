from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader

def index(requests):
    template = loader.get_template('index.html')
    return HttpResponse( template.render())

def about(requests):
    return HttpResponse( 'About page ')