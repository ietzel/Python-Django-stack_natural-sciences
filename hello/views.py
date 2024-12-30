from django.shortcuts import render
from django.http import HttpResponse

t1 = "Ecosphere\nEcosphere, Biome, Ecosystem, Community, Population, Organism.\n"
t2 = "Mars\n"Driver, Flier, Slitherer, Hopper, Crawler, and Runner meet up for the cave exploration mission. The first one drives the other 5 to the cavity, and hoists them down. They find traces of water, and a big place for settlement. Findings reported...\n"
t3 = "Quantum Physics\nHydrogen atom decays to proton + neutrino + photon.\n"
t4 = "Resource Conservation\nFrom a score of 100, deduct 1 for every flush per day above 1, every minute of showering above 5, outlets plugged in above 3, etc.\n"
t5 = "Endangered and Invasive Species\nKeep in mind where they came from, and whether they are keystone species as well.\n"
t6 = "Health\nDeduce away from a score of 100: weekly; for every hour exercised below 7, for every hour slept below 56, for every 125 calories away from 2000.\n"
t7 = "Sleep Cycle\nImagine you are a log in a forest; count sheep to 225 or so.\n"
t8 = "Workoutizer\n1 to 100 of these: burpees, squats, crunches, lunges, planks, etc.\n"

def myView(request):
	return HttpResponse(t1+t2+t3+t4+t5+t6+t7+t8)
