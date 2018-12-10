# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import RoomForm

import map


def index(request):
    return HttpResponse("Hello, world. You're at the game's index.") 


class GameEngine(View):

	def get(self, request):

		# set a session value:
		request.session['room'] = "central corridor"

		form = RoomForm()

		context = {
			'form': form,
		}

		return render(request, 'room.html', context)


	def post(self, request):

		form = RoomForm()

		context = {
			'form': form,
		}

		if form.is_valid():
			pass

			# if form answer == "tell a joke":
				

		# web.config._session = session

		# session.current_level = "central_corridor"

		# if form.action == "tell a joke":
		# 	session.room = map.laser_weapon_armory
		# 	# session.count += 1
		# 	session.current_level = "laser_weapon_armory"
		# 	print str(session.current_level)
		# 	return render.show_room(room=session.room)

		# elif form.action == "0132":
		# 	session.room = map.the_bridge
		# 	# session.count += 1
		# 	session.current_level = "the_bridge"
		# 	print str(session.current_level)
		# 	return render.show_room(room=session.room)

		# elif form.action == "slowly place the bomb":
		# 	session.room = map.escape_pod
		# 	# session.count += 1
		# 	session.current_level = "escape_pod"
		# 	print str(session.current_level)
		# 	return render.show_room(room=session.room)

		# elif form.action == "2":
		# 	session.room = map.the_end_winner
		# 	# session.count += 1
		# 	session.current_level = "the_end_winner"
		# 	print str(session.current_level)
		# 	return render.the_end(room=session.room)

		# else:
		# 	flag = True
		# 	while flag:
		# 		for key, value in deathlist.items():
		# 			if key == str(session.current_level):
		# 				reason = value
		# 				return render.you_died(dead=reason)
		# 				flag = False
		# 		else:
		# 			reason = "You died, bummer!"
		# 			return render.you_died(dead=reason)

		# 	if session.current_level == "central_corridor":
		# 		reason = "You're floating in space infinitely"
		# 		return render.you_died(dead=reason)



		# 	for key, value in deathlist.items():
		# 		if key == session.room:
		# 	return render.you_died()
		# 	session.room = map.generic_death
		# 	return render.you_died(room=session.room)

		# web.seeother("/game")

		return render(request, 'room.html', context)