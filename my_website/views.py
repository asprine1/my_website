from django.shortcuts import render
from django.http import HttpResponse 

def index(requests):
    return HttpResponse( 'first successful page')

def about(requests):
    return HttpResponse( 'About page ')