from django.shortcuts import render
from django.http import HttpResponse

def myView(request):
	return HttpResponse("Driver, Flier, Slitherer, Hopper, Crawler, and Runner meet up for the cave exploration mission. The first one drives the other 5 to the cavity, and hoists them down. They find traces of water, and a big place for settlement. Findings reported...")