#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =========================================================================== #
# IUOC - REDS Institute, HEIG-VD, Yverdon-les-Bains (CH) - 2022               #
# =========================================================================== #
""" simple iuoc - Simple IUOC example

	This example simulates a simple IUOC setup. It has two OCs - 'blind' &
	'thermometer' - and the IuOC Server. They all are mqtt clients.

	The example scenario is the following:
		* The thermometer periodically publish the temperature. The temperature
		  curve is a sinusoidal which varies between 0 and 50 degrees.
		* The server reads the temperature (subscribe to the 'thermometer' topic)
		  and sends the command to the blind OC.
		  The store is close when the temperature is over 30 degrees and close
		  when the temperature is below .
"""
# =========================================================================== #
__author__ = "Jean-Pierre Miceli <jean-pierre.miceli@heig-vd.ch"
# =========================================================================== #

# == system libs
import json
import time
import sys
import threading
import math

# == project libs
from iuoc.iuoc import OC, Data

class Thermometer(object):

	def __init__(self, broker_addr):
		self.oc = OC('thermometer', cluster='debug')
		self.oc.connect(broker_addr)

		# Temperature variables
		self.temp_max = 50
		self.temp_min =  0

		# Start sending the temperature
		thread = threading.Thread(target=self.send_temperature)
		thread.start()

	def send_temperature(self):

		i = 0

		while True:
			# compute temperature
			half_range = (self.temp_max - self.temp_min) / 2
			temperature = self.temp_min + half_range +  (math.sin(i) * half_range)

			data = Data('temperature', temperature)
			self.oc.publish(data)

			i += 0.1
			time.sleep(1)


class Blind(object):

	def __init__(self, broker_addr):
		self.blind = OC('blind', cluster='debug')
		self.blind.connect(broker_addr)

		self.blind.subscribe('iuoc/server/blind_ctrl', self.callback)

	def move(self, direction):
		print("[BLIND] moving %s" % direction)

	def callback(self, client, userdata, message):
		data = json.loads(message.payload)
		value = data['data'][0]['value']

		if value:
			self.move('UP')
		else:
			self.move('Down')

class IUOCServer(object):

	def __init__(self, broker_addr):
		self.server = OC('blind_ctrl', cluster='server')
		self.server.connect(broker_addr)

		# Blind management
		self.current_temp = 0
		self.temp_thr = 30

		self.server.subscribe('iuoc/debug/thermometer', self.thermometer_callback)

	def thermometer_callback(self, client, userdata, message):
		data = json.loads(message.payload)
		value = data['data'][0]['value']

		print("[server] Current temperature: %f degree" % value)

		if value > self.temp_thr and self.current_temp <= self.temp_thr:
			print("[server] Close blind")
			data = Data('UP', False)
			self.server.publish(data)
		elif value < self.temp_thr and self.current_temp >= self.temp_thr:
			print("[server] Open blind")
			data = Data('UP', True)
			self.server.publish(data)

		self.current_temp = value

def main(broker_addr):

	thermometer = Thermometer(broker_addr)
	blind  = Blind(broker_addr)
	server = IUOCServer(broker_addr)

if __name__ == '__main__':

	main('127.0.0.1')
	while True:
		time.sleep(5)

