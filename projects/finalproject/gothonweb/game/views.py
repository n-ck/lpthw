# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import RoomForm

import map

def start(request):

	context = {
		'room': 'Start game',
		'desc': 'Click the button below to start the game'
	}

	return render(request, 'start.html', context)	

class CentralCorridor(View):

	def get(self, request):
		request.session['room'] = "central_corridor"
		form = RoomForm()

		context = {
			'form': form,
			'room': map.central_corridor.name,
			'desc': map.central_corridor.description,
		}

		return render(request, 'room.html', context)


	def post(self, request):
		form = RoomForm(request.POST)

		context = {
			'form': form,
			'room': "",
			'desc': None,
		}

		context['room'] = request.session['room']

		if form.is_valid():
			answer = form.cleaned_data['answer']

			if answer == 'tell a joke':
				print "correct answer"
				request.session['room'] = "laser_weapon_armory"
				context["room"] = map.laser_weapon_armory.name
				context["desc"] = map.laser_weapon_armory.description
				obj = LaserWeaponArmory().get()
				return redirect('laserweaponarmory')

			else:
				context["room"] = "You're dead"
				context["desc"] = "Try again"
				return render(request, 'room.html', context)	


class LaserWeaponArmory(View):

	def get(self, request):

		request.session['room'] = "laser_weapon_armory"

		form = RoomForm(request.GET)

		context = {
			'form': form,
			'room': map.laser_weapon_armory.name,
			'desc': map.laser_weapon_armory.description,
		}

		return render(request, 'room.html', context)


	def post(self, request):

		form = RoomForm(request.POST)

		context = {
			'form': form,
			'room': "",
			'desc': None,
		}

		context['room'] = request.session['room']

		if form.is_valid():
			answer = form.cleaned_data['answer']

			if answer == '0132':
				request.session['room'] = "laser_weapon_armory"
				context["room"] = map.the_bridge.name
				context["desc"] = map.the_bridge.description
				return render(request, 'room.html', context)

			else:
				context["room"] = "Test 123"
				context["desc"] = "Try again"

				return render(request, 'dead.html', context)				

			# elif answer == "0132":
			# 	request.session['room'] = "the_bridge"
			# 	context["room"] = map.the_bridge.name
			# 	context["desc"] = map.the_bridge.description
			# 	return render(request, 'room.html', context)		

			# elif answer == "slowly place the bomb":
			# 	request.session['room'] = "escape_pod"
			# 	context["room"] = map.escape_pod.name
			# 	context["desc"] = map.escape_pod.description
			# 	return render(request, 'room.html', context)

			# elif answer == "2":
			# 	request.session['room'] = "the_end_winner"
			# 	context["room"] = map.the_end_winner.name
			# 	context["desc"] = map.the_end_winner.description
			# 	return render(request, 'room.html', context)		

			# else:
			# 	current_room = request.session['room']

			# 	for key, value in map.generic_death.description.items():

			# 		if current_room == key:
			# 			print current_room
			# 			context["room"] = key
			# 			context["desc"] = value
			# 		else:
			# 			context["room"] = "You're dead"
			# 			context["desc"] = "Blablabla"

			# 	return render(request, 'room.html', context)

		# return render(request, 'room.html', context)


## Final exam:
# - Fix all the bugs I mention in the code, as well as bugs not mentioned
#   - finish the generic_death endings (find the original endings and add back in)
# 	- ???
# - Improve all automated tests
# + Make the HTML better
# - Research logins and create a signup system for the application, so people
#   can login and have high scores
# - Complete the game map, make it as large and feature-complete as possible
# - Give people a help system, that lets them ask what they can do at each room of the game
# - Add any other features you can think of
# - Create several maps and let people choose a game they want to run
# - Use what you learned in Ex48 and Ex49 to create a better input processor (improve the grammar)
